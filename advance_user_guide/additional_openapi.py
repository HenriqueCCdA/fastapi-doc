from fastapi import FastAPI
from fastapi.responses import FileResponse, JSONResponse
from pydantic import BaseModel


class Item(BaseModel):
    id: str
    value: str

class Message(BaseModel):
    message: str

app = FastAPI()


#@app.get(
#    "/items/{item_id}", 
#    response_model=Item, 
#    responses={
#        404: {
#            "model": Message
#        }
#    }
#)
#async def read_item(item_id: str):
#    if item_id == "foo":
#        return {"id": "foo", "value": "there goes my hero"}
#    return JSONResponse(status_code=404, content={"message": "Item not found"})

#@app.get(
#    "/items/{item_id}", 
#    response_model=Item, 
#    responses={
#        200: {
#            "content": {"image/png": {}},
#            "description": "Return the JSON item or an image.",
#        }
#    }
#)
#async def read_item(item_id: str, img: bool | None = None):
#    if img:
#        return FileResponse("image.png", media_type="image/png")
#    else:
#        return {"id": "foo", "value": "there goes my hero"}

#@app.get(
#    "/items/{item_id}", 
#    response_model=Item, 
#    responses={
#        404: {"model": Message, "description": "The item was not found"},
#        200: {
#            "description": "Item request by ID",
#            "content": {
#                "application/png": {
#                    "example": {
#                        "id": "bar",
#                        "value": "The bar tenders"
#                    }
#                }
#            },
#        }
#    }
#)
#async def read_item(item_id: str):
#    if item_id == "foo":
#        return {"id": "foo", "value": "there goes my hero"}
#    else:
#        return JSONResponse(status_code=404, content={"message": "Item not found"})

responses = {
    404: {"description": "Item not found"},
    302: {"description": "The item was moved"},
    403: {"description": "Not  enough privileges"},
}


@app.get(
    "/items/{item_id}", 
    response_model=Item, 
    responses={**responses, 200: {"content": {"image/png": {}}}}
)
async def read_item(item_id: str):
    if item_id == "foo":
        return {"id": "foo", "value": "there goes my hero"}
    else:
        return JSONResponse(status_code=404, content={"message": "Item not found"})
