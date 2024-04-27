from pydantic import BaseModel

class Item(BaseModel):
    item:str

class DBItem(BaseModel):
    items:str
    count:int

class User(BaseModel):
    username: str
    password: str
