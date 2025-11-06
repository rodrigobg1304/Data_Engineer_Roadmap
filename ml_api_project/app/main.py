from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import FastAPI, Path, HTTPException
from enum import Enum
from app.model import Team
from typing import List

app = FastAPI(
    title="ML Model API",
    description="API para servir un modelo de Machine Learning",
    version="0.1.0",
)

class ModelName(str, Enum):
    matches = "matches"
    goals = "goals"
    corners = "corners"

fake_teams_db = [{"item_name": "Real Madrid"}, {"item_name": "Barcelona"},
                 {"item_name": "Sevilla"}, {"item_name": "Real Betis"}]

class TeamName(str, Enum):
    real_madrid = "Real Madrid"
    barcelona = "Barcelona"
    sevilla = "Sevilla"
    betis = "Real Betis"

@app.get("/")
def root():
    return {"message": "Hello World! 🌍"}

@app.get("/ping")
def ping():
    return {"message": "pong 🏓"}

@app.get("/convert_to_binary/{number}")
def convert_to_binary(number: int):
    return {"decimal": number, "binary": bin(number)}

@app.get("/convert_to_decimal/{binary_number}")
def convert_to_decimal(binary_number: str = Path(..., pattern="^[01]+$", description="Binary number (only 0 and 1)")):
    try:
        return {"binary": binary_number, "decimal": int(binary_number, 2)}
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid binary number, check it")

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name.value == ModelName.matches:
        return {"model_name": model_name, "message": "Deep matches results"}
    elif model_name.value == ModelName.goals:
        return {"model_name": model_name, "message": "Deep goals results"}
    elif model_name.value == ModelName.corners:
        return {"model_name": model_name, "message": "Deep corners results"}
    else:
        return {"model_name": model_name, "message": "No matched with the model selected."}

@app.get("/teams/")
async def get_teams(skip: int = 0, limit: int = 10):
    return fake_teams_db[skip : skip + limit]

@app.post("/teams/")
async def post_teams(teams: List[Team]):
    return {"message": "Created", "total": len(teams), "data": teams}


@app.get("/team_info/{team_name}")
async def get_team_info(team_name: TeamName, needy: str, skip: int = 0, limit: int | None = None, q: str | None = None):
    if q in team_name:
        item = {"Team": team_name, "needy": needy, "skip": skip, "limit": limit, "Query": q}
        return item
    else:
        return {"Team": team_name, "needy": needy, "skip": skip, "limit": limit}

