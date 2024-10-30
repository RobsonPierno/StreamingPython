from datetime import datetime
from typing import List
from pydantic import BaseModel, Field

class Filme(BaseModel):
    id: int
    name: str
    dt_release: datetime = Field(alias = "dtRelease")
    gender: str
    director: str
    dt_insert: datetime = Field(alias = "dtInsert")
    active: bool
    pessoa: int = Field(alias = "idPessoa")

class Filmes(BaseModel):
    filmes: List[Filme]