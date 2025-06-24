from pydantic import BaseModel


class Live(BaseModel):
    live: bool
    title: str
