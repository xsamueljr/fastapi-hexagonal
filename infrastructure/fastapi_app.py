from fastapi import FastAPI

from infrastructure.dependencies import users_router

app = FastAPI()

app.include_router(users_router)
