from pydantic import BaseModel
from enum import Enum

class Country(str, Enum):
    spain = "Spain"
    portugal = "Portugal"
    france = "France"
    england = "England"
    italy = "Italy"

class Team(BaseModel):
    name: str
    country: Country
    division: int
    city: str