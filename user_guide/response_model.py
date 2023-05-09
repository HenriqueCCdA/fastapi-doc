from typing import Any
from fastapi import FastAPI, Response
from fastapi.applications import JSONResponse
from fastapi.responses import RedirectResponse
from pydantic import BaseModel, EmailStr

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float = 10.5


items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The Bar fighters", "price": 60, "tax": 20.2},
    "baz": {
        "name": "Baz",
        "description": "There goes my baz",
        "price": 50.2,
        "tax": 10.5,
    }
}


@app.get(
    "/items/{item_id}/name",
    response_model=Item,
    response_model_include={"name", "description"},
)
async def read_item_name(item_id: str):
    return items[item_id]


@app.get("/items/{item_id}/public", response_model=Item, response_model_exclude={"tax"})
async def read_item_public_data(item_id: str):
    return items[item_id]


#class Item(BaseModel):
#    name: str
#    description: str | None = None
#    price: float
#    tax: float = 10.5
#    tags: list[str] = []
#
#
#items = {
#    "foo": {"name": "Foo", "price": 50.2},
#    "bar": {"name": "Bar", "description": "The bartenders", "price": 50.2, "tax": 20.2},
#    "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
#}
#
#
#class BaseUser(BaseModel):
#    username: str
#    email:  EmailStr
#    full_name:  str | None = None
#
#
#class UserIn(BaseUser):
#    password: str


#@app.post("/portal/")
#async def get_portal(teleport: bool = False) -> Response:
#    if teleport:
#        return RedirectResponse(url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")
#    return JSONResponse(content={"message": "Here's your interdimensional portal."})


##@app.post("/portal/", response_model=None)
##async def get_portal(teleport: bool = False) -> Response | dict:
##    if teleport:
##        return RedirectResponse(url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")
##    return {"message": "Here's your interdimensional portal."}
##
##
##@app.post("/user/")
##async def create_user(user: UserIn) -> BaseUser:
##    return user
##
##@app.get("/items/{item_id}", response_model=Item, response_model_exclude_unset=True)
##async def read_item(item_id: str):
##    return items[item_id]


#class Item(BaseModel):
#    name: str
#    description: str | None = None
#    price: float
#    tax: float | None = None
#    tags: list[str] = []
#
#
#class UserIn(BaseModel):
#    username: str
#    password: str
#    email: EmailStr
#    full_name: str | None = None
#
#class UserOut(BaseModel):
#    username: str
#    email: EmailStr
#    full_name: str | None = None
#
#
#@app.post("/items/")
#async def create_item(item: Item) -> Item:
#    return item
#
#
#@app.get("/items/")
#async def read_items() -> list[Item]:
#    return [
#        Item(name="Portal Gun", price=42.0),
#        Item(name="Plumbus", price=32.0),
#    ]
#
#@app.post("/v2/items/", response_model=Item)
#async def create_item2(item: Item) -> Any :
#    return item
#
#
#@app.get("/v2/items/", response_model=list[Item])
#async def read_items2() -> Any:
#    return [
#        {"name": "Portal Gun", "price": 42.0},
#        {"name": "Plumbus", "price": 32.0},
#    ]
#
#
#@app.post("/user/", response_model=UserOut)
#async def create_user(user: UserIn) -> Any:
#    return user
