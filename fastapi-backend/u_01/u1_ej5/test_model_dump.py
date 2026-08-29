from pydantic import BaseModel

class item(BaseModel):
    name: str
    price: float

item = item(name="cafetera", price=120.0)
item_id = 505
#item_dict = item.model_dump()
#print(item_dict)
resultado = {"item_id": item_id, **item.model_dump()}
print(resultado)