from fastapi import FastAPI, Request

app = FastAPI(
    servers=[
        {"url": "https://stag.example.org", "description": "Staging enviroment"},
        {"url": "https://stag.example.org", "description": "Staging enviroment"},
    ],
    root_path="/api/v1"
)


@app.get("/app")
def read_main(request: Request):
    return {"message": "Hello World", "root_path": request.scope.get("root_path")}
