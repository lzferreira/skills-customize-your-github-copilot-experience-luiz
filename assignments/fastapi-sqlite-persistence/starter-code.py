from contextlib import closing
from pathlib import Path
import sqlite3

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="Books API")
DB_PATH = Path(__file__).with_name("books.db")


class Book(BaseModel):
    id: int
    title: str = Field(min_length=1)
    author: str = Field(min_length=1)


class BookInput(BaseModel):
    title: str = Field(min_length=1)
    author: str = Field(min_length=1)


def get_connection():
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    return connection


def initialize_database():
    with closing(get_connection()) as connection:
        pass


initialize_database()


# Implement the books routes below.
