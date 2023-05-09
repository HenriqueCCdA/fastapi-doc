from fastapi import FastAPI
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi.middleware.gzip import GZipMiddleware

app = FastAPI()

app.add_middleware(GZipMiddleware, minimum_size=1)
#app.add_middleware(TrustedHostMiddleware, allowed_hosts=["exemple.com"])
#app.add_middleware(HTTPSRedirectMiddleware)
#
#

@app.get("/")
async def main():
    return {"message": "Hello World"}
