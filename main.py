from typing import Union

from fastapi import Depends, FastAPI
from pydantic import BaseModel

from sqlalchemy import text
from sqlalchemy.orm import Session
from src.database import get_db

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}


@app.get("/raw-query/")
def raw_query(db: Session = Depends(get_db)):
    raw_sql = text("SELECT * FROM courses")

    result = db.execute(raw_sql)

    column_names = result.keys()

    rows = result.fetchall()

    data = [dict(zip(column_names, row)) for row in rows]

    return {"data": data}
