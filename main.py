import time
import logging
from fastapi import FastAPI, Request
from routers import router
from starlette.middleware.base import BaseHTTPMiddleware
from middlewares import ContentTypeLogger

app = FastAPI(
    title="BaseApp",
    description=("BaseApp"),
    version="0.1",
    docs_url="/docs",
    redoc_url="/docs/redoc",
)


app.include_router(router)
my_middleware = ContentTypeLogger()


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response


app.add_middleware(BaseHTTPMiddleware, dispatch=my_middleware)
