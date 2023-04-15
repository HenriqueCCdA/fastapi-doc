from typing import Annotated
from fastapi import FastAPI, Query


app = FastAPI()


# @app.get("/items/")
# async def read_items(q: str | None = None):
#     results = {"item": [{"item_id": "Foo"}, {"item_id": "Bar"}]}

#     if q:
#         results.update({"q": q})

#     return results

# @app.get("/items/")
# async def read_items(q: Annotated[str | None, Query(min_length=3, max_length=10)] = None):
#     results = {"item": [{"item_id": "Foo"}, {"item_id": "Bar"}]}

#     if q:
#         results.update({"q": q})

#     return results


# @app.get("/items/")
# async def read_items(q: Annotated[str | None, Query(min_length=3, max_length=10, regex="^fixedquery$")] = None):
#     results = {"item": [{"item_id": "Foo"}, {"item_id": "Bar"}]}

#     if q:
#         results.update({"q": q})

#     return results


# @app.get("/items/")
# async def read_items(q: Annotated[str | None, Query(min_length=3)] = "fixedquery"):
#     results = {"item": [{"item_id": "Foo"}, {"item_id": "Bar"}]}

#     if q:
#         results.update({"q": q})

#     return results


# @app.get("/items/")
# async def read_items(q: Annotated[str, Query(min_length=3)]):
#     results = {"item": [{"item_id": "Foo"}, {"item_id": "Bar"}]}

#     if q:
#         results.update({"q": q})

#     return results


# @app.get("/items/")
# async def read_items(q: Annotated[str | None, Query(min_length=3)] = ...):
#     results = {"item": [{"item_id": "Foo"}, {"item_id": "Bar"}]}

#     if q:
#         results.update({"q": q})

#     return results


# @app.get("/items/")
# async def read_items(q: Annotated[list[str] | None, Query()] = None):
#     results = {"item": [{"item_id": "Foo"}, {"item_id": "Bar"}]}

#     if q:
#         results.update({"q": q})

#     return results

# @app.get("/items/")
# async def read_items(q: Annotated[list[str], Query()] = ["foo", "bar"]):
#     results = {"item": [{"item_id": "Foo"}, {"item_id": "Bar"}]}

#     if q:
#         results.update({"q": q})

#     return results


# @app.get("/items/")
# async def read_items(
#     q: Annotated[
#         str | None,
#         Query(
#             title="Query string",
#             description="Query string for the items to search in the database that have a good match",
#             min_length=3
#         )
#     ] = None
# ):
#     results = {"item": [{"item_id": "Foo"}, {"item_id": "Bar"}]}

#     if q:
#         results.update({"q": q})

#     return results


# @app.get("/items/")
# async def read_items(q: Annotated[str | None, Query(alias="item-query")] = None):
#     results = {"item": [{"item_id": "Foo"}, {"item_id": "Bar"}]}

#     if q:
#         results.update({"q": q})

#     return results


# @app.get("/items/")
# async def read_items(
#     q: Annotated[
#         str | None,
#         Query(
#             alias="item-query",
#             title="Query string",
#             description="Query string for the items to search in the database that have a good match",
#             min_length=3,
#             max_length=50,
#             deprecated=True
#         )
#     ] = None
# ):
#     results = {"item": [{"item_id": "Foo"}, {"item_id": "Bar"}]}

#     if q:
#         results.update({"q": q})

#     return results

@app.get("/items/")
async def read_items(
        hidden_query: Annotated[str | None, Query(include_in_schema=False)] = None
):

    if hidden_query:
        return {"hidden_query": hidden_query}
    else:
        return {"hidden_query": "not found"}
