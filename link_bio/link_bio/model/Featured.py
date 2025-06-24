from pydantic import BaseModel


class Featured(BaseModel):
    title: str
    image: str
    url: str
