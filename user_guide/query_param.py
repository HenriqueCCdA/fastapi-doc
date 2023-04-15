from fastapi import FastAPI

app = FastAPI()

fake_item_db = [
    {"item_name": "Foo"},
    {"item_name": "Bar"},
    {"item_name": "Baz"},
]


# @app.get("/items/")
# async def read_item(skip: int = 0, limit: int = 10):
#     return fake_item_db[skip : skip + limit]


# @app.get("/items/{item_id}")
# async def read_item2(item_id: str, q: str | None = None):
#     if q:
#         return {"item_id": item_id, "q": q}
#     return {"item_id": item_id}


# @app.get("/items2/{item_id}")
# async def read_item3(item_id:  str, q: str | None = None, short: bool = False):
#     item = {"item_id": item_id}

#     if q:
#         item.update({"q": q})
#     if not short:
#         item.update(
#             {"description": "This is an amazing item that a long description"}
#         )
#     return item


# @app.get("/users/{user_id}/items/{item_id}")
# async def read_user_item(
#     user_id: int, item_id: str, q: str | None = None, short = False
# ):
#     item = {"item_id": item_id, "owner_id": user_id}

#     if q:
#         item.update({"q": q})

#     if not short:
#         item.update(
#             {"description": "This is an amazing item that a long description"}
#         )

#     return item

# @app.get("/items/{item_id}")
# async def read_user_item(item_id:str, needy: str):
#     item = {"item": item_id, "needy": needy}
#     return item

@app.get("/items/{item_id}")
async def read_user_item(item_id:str, needy: str, skip: int = 0, limit: int | None = None):
    item = {"item": item_id, "needy": needy, "skip": skip, "limit": limit}
    return item
