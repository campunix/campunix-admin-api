from typing import TypeVar, Type, Dict, Any, List

from pydantic import BaseModel, ValidationError

T = TypeVar("T", bound=BaseModel)


def entity_to_model(entity: object, model: Type[T]) -> T:
    if entity is None:
        return None
    else:
        try:
            return model(**entity.__dict__)
        except ValidationError as e:
            print(repr(e.errors()))
            raise Exception(e)
        except Exception as e:
            print(e)
            raise Exception(e)


def entities_to_model(entities: List[object], model: Type[T]) -> List[T]:
    if not entities:
        return None
    else:
        merged_entities: Dict[str, Any] = {}
        for entity in entities:
            merged_entities.update(entity)

        print(merged_entities)
        return [model(**merged_entities)]


def entity_to_model_list(
        entity_dict: Dict[str, Any],
        model: Type[T],
        paginate: bool = False
) -> Dict[str, Any]:
    items = entity_dict.get("items", [])

    try:
        # model_list = [model(**item) for item in items]
        model_list = [
            model(**convert_nested_fields(item, model))
            for item in items
        ]
    except ValidationError as e:
        print(repr(e.errors()))
        raise Exception(e)
    except Exception as e:
        print(e)
        raise Exception(e)

    if paginate:
        return {
            "items": model_list,
            "current_page": entity_dict.get("current_page"),
            "total_pages": entity_dict.get("total_pages"),
            "page_size": entity_dict.get("page_size"),
            "total_items": entity_dict.get("total_items")
        }
    else:
        return {
            "items": model_list,
        }


def convert_nested_fields(item: Dict[str, Any], model: Type[BaseModel]) -> Dict[str, Any]:
    item_dict = {}
    for field, field_type in model.__annotations__.items():
        if hasattr(field_type, '__name__') and field_type.__name__ == 'Type':
            # Skip type annotations that are not models (e.g., primitive types)
            continue
        if issubclass(field_type, BaseModel):
            # If the field is a model, recursively convert it
            item_dict[field] = field_type(**item[field]) if field in item else None
        else:
            # Otherwise, directly assign the field value
            item_dict[field] = item.get(field)
    return item_dict
