from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(title="Books API")


class Book(BaseModel):
    id: int
    title: str = Field(min_length=1)
    author: str = Field(min_length=1)


class BookInput(BaseModel):
    title: str = Field(min_length=1)
    author: str = Field(min_length=1)


books = [
    Book(id=1, title="A Wizard of Earthsea", author="Ursula K. Le Guin"),
    Book(id=2, title="The Left Hand of Darkness", author="Ursula K. Le Guin"),
]


# Add your API routes below.
