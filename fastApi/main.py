from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"message": "Hello " + item_id}

@app.get("/names/{name}")
async def read_item(name: str):
    return {"message": "Hello " + name}