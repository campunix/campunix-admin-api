from typing import TypeVar, Type, Dict, Any

from pydantic import BaseModel

T = TypeVar("T", bound=BaseModel)


def entity_to_model(entity: object, model: Type[T]) -> T:
    if entity is None:
        return None
    else:
        return model(**entity.__dict__)


def entity_to_model_list(
        entity_dict: Dict[str, Any],
        model: Type[T],
        paginate: bool = False
) -> Dict[str, Any]:
    items = entity_dict.get("items", [])
    model_list = [model(**item.__dict__) for item in items]

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
