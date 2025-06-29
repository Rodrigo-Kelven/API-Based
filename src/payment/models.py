from pydantic import BaseModel, conint, confloat
from typing import List


class Item(BaseModel):
    title: str
    quantity: conint(gt=0)  # deve ser inteiro > 0
    unit_price: confloat(gt=0.0) # deve ser float > 0.0


class Carrinho(BaseModel):
    items: List[Item]