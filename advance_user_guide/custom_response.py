from typing import Any
from fastapi import FastAPI, Response
from fastapi.responses import FileResponse, HTMLResponse, ORJSONResponse, PlainTextResponse, RedirectResponse, StreamingResponse
import orjson

app = FastAPI()


#@app.get("/item/", response_class=ORJSONResponse)
#async def read_items():
#    return ORJSONResponse([{"item_id": "Foo"}])
#
#
#@app.get("/items/", response_class=HTMLResponse)
#async def read_items2():
#    return """
#    <html>
#        <head>
#            <title>Some HTML in there</title>
#        </head>
#        <body>
#            <h1>Look ma! HTML!</h1>
#        </body>
#    </html>
#    """

def generate_html_response():
    html_content = """
    <html>
        <head>
            <title>Some HTML in here</title>
        </head>
        <body>
            <h1>Look ma! HTML!</h1>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)


@app.get("/items/", response_class=HTMLResponse)
async def read_items():
    return generate_html_response()


@app.get("/legacy/")
def get_legacy_data():
    data = """<?xml version="1.0"?>
    <shampoo>
    <Header>
        Apply shampoo here.
    </Header>
    <Body>
        You'll have to use soap here.
    </Body>
    </shampoo>
    """
    return Response(content=data, media_type="application/xml")


#@app.get("/", response_class=PlainTextResponse)
#async def main():
#    return "Hello World"


@app.get("/typer")
async def redirect_type():
    return RedirectResponse("https://typer.tiangolo.com")


@app.get("/fastapi", response_class=RedirectResponse)
async def redirect_fastapi():
    return "https://FastAPI.tiangolo.com"


async def fake_video_streamer():
    for _ in range(10):
        yield b"some fake video bytes"

#@app.get("/")
#async def main():
#    return StreamingResponse(fake_video_streamer())


some_file_path = "cut_cali.mp4"


#@app.get("/")
#def main():
#    def iterfile():
#        with open(some_file_path, mode="rb") as file_like:
#            yield from file_like
#
#    return StreamingResponse(iterfile(), media_type="video/mp4")


#@app.get("/", response_class=FileResponse)
#async def main():
#    return some_file_path

class CustomORJSONResponse(Response):
    media_type = "application/json"

    def render(self, content: Any) -> bytes:
        assert orjson is not None, "orjson must be installed"
        return orjson.dumps(content, option=orjson.OPT_INDENT_2)

@app.get("/", response_class=CustomORJSONResponse)
async def main():
    return {"message": "Hello World"}

