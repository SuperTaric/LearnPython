from typing import Union
from fastapi import FastAPI
from enum import Enum
from pydantic import BaseModel

class ModelName(str, Enum):
    alexnet = 'alexnet'
    resnet = 'resnet'
    lenet = 'lenet'

class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None

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

@app.get("models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Leaarning FTW"}
    
    if model_name.value == 'lenet':
        return {"model_name": model_name, "message": "LeCNN all the images"}
    
    return {"model_name": model_name, "message": "Have some residuals"}

@app.post("/items/")
async def create_item(item: Item):
    item_dict = item.dict()
    if (item.tax):
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    print(item.name)
    return item_dict