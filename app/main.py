from fastapi import FastAPI
from .routers import user_routes

app=FastAPI()

@app.get("/")
def get_root():
    return{"message":"FastApi is running"}

app.include_router(user_routes.router)