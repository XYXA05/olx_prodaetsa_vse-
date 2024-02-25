from typing import Union, Optional
from uuid import UUID, uuid4 
from fastapi import FastAPI 
from pydantic import BaseModel, Field 
from enum import Enum
from typing import List

app = FastAPI()

class Items_Search(BaseModel):
    model: str
    price_hight: int
    price_low: int
    use: int
    city: str

class Item(BaseModel):
    items_search_id: str
    name_url: str
    price_url: str
    meet_url: str
    url: str