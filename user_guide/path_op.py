
from enum import Enum
from typing import Union
from typing_extensions import deprecated

from fastapi import FastAPI, status
from pydantic import BaseModel


app = FastAPI()


class Item(BaseModel):
    name: str
    ddescription: Union[str, None] = None
    price: float
    tax: Union[float, None] = None
    tags: set[str] = set()


class Tags(Enum):
    items = "items"
    users = "users"

#@app.post("/items/", response_model=Item, status_code=status.HTTP_201_CREATED)
#async def create_item(item: Item):
#    return item

#@app.post(
#    "/items/", 
#    response_model=Item, 
#    tags=[Tags.items],
#    summary="Create an item",
#    description="Create an item with all the information name, description, price, tax and a set of unique tags."
#)
#async def create_item(item: Item):
#    return item

@app.post(
    "/items/", 
    response_model=Item, 
    summary="Create an item",
    response_description="The create item",
)
async def create_item(item: Item):
    """
    Create an item with all the information

    - **name**: each item must have a name
    - **description**: a long description
    - **price**: required
    - **tax**: if the item doesn't have tax, you can omit this
    - **tags**: a set of unique tag strings for this item
    """
    return item


@app.get("/items/", tags=["items"])
async def read_items():
    return [{"name": "Foo", "price": 42}]


@app.get("/users/", tags=[Tags.users], deprecated=True)
async def read_users():
    return [{"username": "johndoe"}]
