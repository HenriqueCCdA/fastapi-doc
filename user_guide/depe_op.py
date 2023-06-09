from typing import Annotated

from fastapi import Depends, FastAPI, Header, HTTPException


async def verify_token(x_token: Annotated[str, Header()]):
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")


async def verify_key(x_key: Annotated[str, Header()]):
    if x_key != "fake-super-secret-key":
        raise HTTPException(status_code=400, detail="X-Key header invalid")
    return x_key


#@app.get("/items/", dependencies=[Depends(verify_token), Depends((verify_key))])
#async def read_item():
#    return [{"item": "Foo"}, {"item": "Bar"}]


app = FastAPI(dependencies=[Depends(verify_token), Depends(verify_key)])


@app.get("/users/")
async def read_users():
    return [{"username": "Rick"}, {"username": "Plumbus"}]


@app.get("/items/")
async def read_items():
    return [{"item": "Portal Gun"}, {"item": "Plumbus"}]
