from fastapi import FastAPI
import uvicorn

import schema
from database import engine
from routers import *
from middleware import log_middleware
from starlette.middleware.base import BaseHTTPMiddleware


app = FastAPI()
app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)
app.add_middleware(BaseHTTPMiddleware, dispatch=log_middleware)


# Creates tables if doesn't exist
schema.Base.metadata.create_all(bind = engine)


if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=False)