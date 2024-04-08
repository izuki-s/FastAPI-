from typing import Optional, List
from fastapi import FastAPI
from pydantic import BaseModel,Field

class ShopInfo(BaseModel):
    name: str
    location: str

class Item(BaseModel):
    name: str = Field(min_length=4, max_length=14)
    description: Optional[str] = None
    price: int
    tax: Optional[float] = None

class Data(BaseModel):
    shop_info: Optional[ShopInfo] = None
    items:  List[Item]

app = FastAPI()

@app.post("/item")
async def create_item(data: Data):
    return {"data":data}





