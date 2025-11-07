from pydantic import BaseModel
from enum import Enum

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: list[str] = []

class CommonHeaders(BaseModel):
    # model_config = {"extra": "forbid"}

    host: str
    save_data: bool
    if_modified_since: str | None = None
    traceparent: str | None = None
    x_tag: list[str] = []

class Country(str, Enum):
    spain = "Spain"
    portugal = "Portugal"
    france = "France"
    england = "England"
    italy = "Italy"

class ModelName(str, Enum):
    matches = "matches"
    goals = "goals"
    corners = "corners"

class Team(BaseModel):
    name: str
    country: Country
    division: int
    city: str
    tags: list[str] = []

class TeamName(str, Enum):
    real_madrid = "Real Madrid"
    barcelona = "Barcelona"
    sevilla = "Sevilla"
    betis = "Real Betis"