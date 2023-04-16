from typing import Annotated, Any

from fastapi import Body, FastAPI, Path
from pydantic import BaseModel


app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


class User(BaseModel):
    username: str
    full_name: str | None = None


@app.put("/items/{item_id}")
async def update_item(
    item_id: Annotated[int, Path(title="The ID of the item to get", ge=0, le=1000)],
    item: Item | None = None,
    q1: str | None = None,
    q2: str | None = None,
):

    results: dict[str, Any] = {"item_id": item_id}

    if q1:
        results.update({"q1": q1})

    if q2:
        results.update({"q2": q2})
    
    if item:
        results.update({"item": item})

    return results


@app.put("/items2/{item_id}")
async def update_item2(item_id: int, item: Item, user: User):
    results = {"item_id": item_id, "item": item, "user": user}

    return results

@app.put("/items3/{item_id}")
async def update_item3(
    item_id: int, 
    item: Item, 
    user: User,
    importance: Annotated[int, Body()]
):
    results = {"item_id": item_id, "item": item, "user": user, "importance": importance}

    return results

@app.put("/items4/{item_id}")
async def update_item4(
    item_id: int, 
    item: Item, 
    user: User,
    importance: Annotated[int, Body(gt=0)],
    q: str | None = None,
 ):
    results = {"item_id": item_id, "item": item, "user": user, "importance": importance}
 
    if q:
        results.update({"q": q})

    return results

@app.put("/items5/{item_id}")
async def update_item5(item_id: int, item: Annotated[Item, Body(embed=True)]):

    results = {"item_id": item_id, "item": item}
 
    return results
