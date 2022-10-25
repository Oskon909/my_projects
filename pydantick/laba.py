from pydantic import BaseModel



class taf(BaseModel):
    alisa:int
    money :int

class sadi(BaseModel):
    number: int
    name: str
    age :int
    targarien:list[taf]

date_json = """
{
    "number": 708,
    "name": "1",
    "age": 1000,
    "targarien":[{"alisa":12,"money":10222}]
}
"""
aser = sadi.parse_raw(date_json)
print(aser.json())
