from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import FastAPI, Path, HTTPException, Query, Header
from enum import Enum
from app.model import Team, ModelName, TeamName, CommonHeaders, Item
from typing import List, Annotated, Any

app = FastAPI(
    title="ML Model API",
    description="API para servir un modelo de Machine Learning",
    version="0.1.0",
)

fake_teams_db = [{"item_name": "Real Madrid"}, {"item_name": "Barcelona"},
                 {"item_name": "Sevilla"}, {"item_name": "Real Betis"}]

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
    """
    Select the model that you want to implement
    :param model_name: Enum of different values.
    :return: json structure
    """
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
async def post_teams(teams: List[Team]) -> Any:
    return {"message": "Created", "total": len(teams), "data": teams}


@app.get("/team_info/{team_name}")
async def get_team_info(team_name: TeamName, needy: str, skip: int = 0, limit: int | None = None, q: str | None = None):
    if q in team_name:
        item = {"Team": team_name, "needy": needy, "skip": skip, "limit": limit, "Query": q}
        return item
    else:
        return {"Team": team_name, "needy": needy, "skip": skip, "limit": limit}

@app.get("/items/")
async def read_items(
    q: Annotated[
        str | None,
        Query(
            alias="item-query",
            title="Query string",
            description="Query string for the items to search in the database that have a good match",
            min_length=3,
            max_length=50,
            pattern="^fixedquery$",
            deprecated=True,
        ),
    ] = None,
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

@app.get("/headers/")
async def get_headers(headers: Annotated[CommonHeaders, Header(convert_underscores=False)]):
    return headers

@app.post("/items2/", response_model=Item)
async def create_item(item: Item) -> Any:
    return item


@app.get("/items2/", response_model=list[Item])
async def read_items() -> Any:
    return [
        {"name": "Portal Gun", "price": 42.0},
        {"name": "Plumbus", "price": 32.0},
    ]


# app/main.py
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI()

# Cargar el modelo entrenado al iniciar
model = joblib.load("app/model_rf.pkl")
iris_classes = ["setosa", "versicolor", "virginica"]

# Definir el esquema de entrada con Pydantic
class IrisFeatures(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

@app.post("/predict/")
async def predict(iris: IrisFeatures):
    # Convertir los datos a numpy array
    features = np.array([[iris.sepal_length, iris.sepal_width, iris.petal_length, iris.petal_width]])
    prediction = model.predict(features)[0]
    pred_idx = model.predict(features)[0]
    return {"prediction": int(prediction), "flower": iris_classes[pred_idx]}
