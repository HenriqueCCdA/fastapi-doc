from typing import Callable

from fastapi import Body, FastAPI, HTTPException, Request, Response
from fastapi.exceptions import RequestValidationError
from fastapi.routing import APIRoute


class ValidationErrorLoggingRoute(APIRoute):
    def gett_route_handler(self) -> Callable:
        original_router_handler = super().get_route_handler()

        async def custom_route_handler(request: Request) -> Response:
            try:
                return await original_router_handler(request)
            except RequestValidationError as exc:
                body = await request.body()
                detail = {"errors": exec.errors(), "body": body.decode()}
                raise HTTPException(status_code=422, detail=detail)

        return custom_route_handler


app = FastAPI()
app.router.route_class = ValidationErrorLoggingRoute


@app.post("/")
async def sum_numbers(numbers: list[int] = Body()):
    return sum(numbers)
