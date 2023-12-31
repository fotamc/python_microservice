"""Module docstring"""
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root():
    """funtion docstring"""
    return {"message": "Hello World"}


@app.get("/data/{name}")
async def read_data(name: str):
    """funtion docstring"""
    return {"message": f"Hello World {name.capitalize()}"}
