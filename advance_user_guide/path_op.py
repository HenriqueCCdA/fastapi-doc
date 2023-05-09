#from typing import Set, Union

#from fastapi import FastAPI, Request
#from fastapi.routing import APIRoute

import yaml
from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel, ValidationError


app = FastAPI()


class Item(BaseModel):
    name: str
    tags: list[str]


@app.post(
    "/items/",
    openapi_extra={
        "requestBody": {
            "content": {"apllication/x-yaml": {"schema": Item.schema()}},
            "required": True,
        },
    },
)
async def create_item(request: Request):
    raw_body = await request.body()
    try:
        data = yaml.safe_load(raw_body)
    except yaml.YAMLError:
        raise HTTPException(status_code=422, detail="Invalid YAML")

    try:
        item = Item.parse_obj(data)
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=e.errors())

    return item



#def magic_data_reader(row_body: bytes):
#    return {
#        "size": len(row_body),
#        "content": {
#            "price": 42,
#            "description": "Just kiddin', no magic here. ✨", 
#        },
#    }
#
#
#@app.post(
#    "/items/",
#    openapi_extra={
#        "requestBody": {
#            "content": {
#                "application/json": {
#                    "schema": {
#                        "required": ["name", "price"],    
#                        "type": "object",    
#                        "properties": {
#                            "name": {"type": "string"},
#                            "price": {"type": "number"},
#                            "description": {"type": "string"},
#                        },    
#                        "required": ["name", "price"],    
#                    }
#                }
#            }
#        }
#    },
#)
#async def create_item(request: Request):
#    raw_body = await request.body()
#    data = magic_data_reader(raw_body)
#    return data
#


#class Item(BaseModel):
#    name: str
#    desciption: Union[str, None] = None
#    price: float
#    tax: Union[float, None] = None
#    tags: Set[str] = set()
#
#
#@app.post("/items/", response_model=Item, summary="Create an item", openapi_extra={"x-aperture-labs-portal": "blue"})
#async def create_item(item: Item):
#    """
#    Create an item with all the information:
#
#    - **name***: each item must have a name
#    - **desciption***: a long description
#    - **price***: required
#    - **tax***: if the item doesn't have tax, you can omit this
#    \f
#    :param item: User input
#    """
#    return item



#@app.get("/items/", operation_id="some_specific_id_you_define")
#async def read_items():
#    return [{"item_id": "Foo"}]

#@app.get("/items/", include_in_schema=False)
#async def read_items():
#    return [{"item_id": "Foo"}]
#
#def user_route_names_as_operation_ids(app:FastAPI) -> None:
#
#    for route in app.routes:
#        if isinstance(route, APIRoute):
#            route.operation_id = route.name
#
#
#user_route_names_as_operation_ids(app)
