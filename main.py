from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    num1: str
    num2: str
    op: str


class Result(BaseModel):
    result: str


class MagicMathService:
    def __init__(self, url) -> None:
        # Init external service
        self.url = url

    def execute(self, item):
        op = item.num1 + item.op + item.num2
        sln = eval(op)
        return sln


@app.post("/")
async def main_route(item: Item):
    math_service = MagicMathService("https://calculator.io")

    result = Result(result=math_service.execute(item))

    return result
