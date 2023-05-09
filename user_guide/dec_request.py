from typing import Annotated
from fastapi import FastAPI, Body
from pydantic import BaseModel, Field

app = FastAPI()


#class Item(BaseModel):
#    name: str
#    description: str | None = None
#    price: float
#    tax: float | None = None
#
#    class Config:
#        schema_extra = {
#            "example": {
#                "name": "Foo",
#                "description": "A very nice Item",
#                "price": 35.4,
#                "tax": 3.2
#            }
#        }

#class Item(BaseModel):
#    name: str = Field(example="Foo")
#    description: str | None = Field(default=None, example="A very nive Item")
#    price: float = Field(example=35.4)
#    tax: float | None = Field(default=None, example=3.2)
#
#
#@app.put("/items/{item_id}")
#async def update_item(item_id: int, item: Item):
#    results = {"item_id": item_id, "item": item}
#    return results


class Item(BaseModel):
    name: str
    description: str | None
    price: float
    tax: float | None


@app.put("/items/{item_id}")
async def update_item(
    item_id: int,
    item: Annotated[
        Item,
        Body(
            examples={
                "normal":{
                    "summary": "A normal example",
                    "description": "A **normal** item works correctly",
                    "values": {
                        "name": "Foo",
                        "description": "A very nice Item",
                        "price": 35.4,
                        "tax": 3.2,
                    },
                },
                "converted":{
                    "summary": "An example with converted data",
                    "description": "FastAPI can concert price strings to actual numbers",
                    "values": {
                        "name": "Foo",
                        "price": "35.4",
                    },
                },
                "invalid":{
                    "summary": "Invalid data is rejected with an error",
                    "values": {
                        "name": "Baz",
                        "price": "thirty fivee point four",
                    },
                },
            },
        ),
    ],
):
    results = {"item_id": item_id, "item": item}
    return results
