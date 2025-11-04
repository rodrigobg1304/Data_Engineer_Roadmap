------

# Plan 8 semanas Data Engineer

## 🧭 **1. Objetivo General**

**En 8 semanas** tendrás un **proyecto completo** que incluye:

1. Entrenamiento y serialización de un modelo ML.
2. API REST con FastAPI que sirva el modelo.
3. Contenedor Docker con todo el entorno.
4. Gestión de dependencias moderna con **uv**.
5. Bonus: preparación para escalar hacia **Airflow / Databricks / MLOps**.

------

## 🗓️ **2. PLAN DE ESTUDIO Y PROYECTO — 8 SEMANAS**

### 🔹 **SEMANA 1 — Entorno y Setup Moderno**

**Objetivo:** Familiarizarte con `uv`, Docker y estructura de proyecto productivo.

**Conceptos:**

- Crear entornos con `uv` → [Docs oficiales](https://docs.astral.sh/uv/pip/environments/#using-a-virtual-environment)
- Crear un `Dockerfile` básico y entender imágenes, capas, y volúmenes.
- Usar VSCode + Dev Containers o PyCharm con Docker.

**Práctica:**

- Monta un proyecto `ml_api_project/` con esta estructura:

  ```
  ml_api_project/
  ├── app/
  │   ├── main.py
  │   ├── model.py
  │   └── utils.py
  ├── requirements.txt
  ├── Dockerfile
  ├── README.md
  └── tests/
  ```

- Crea un entorno `uv`:

  ```
  uv venv
  uv pip install fastapi uvicorn scikit-learn pandas joblib
  ```

- Crea un `Dockerfile` que construya y ejecute una app FastAPI mínima:

  ```
  FROM python:3.11-slim
  WORKDIR /app
  COPY . .
  RUN pip install uvicorn fastapi
  CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
  ```

------

### 🔹 **SEMANA 2 — FastAPI en Profundidad**

**Objetivo:** Construir tu primera API REST funcional.

**Conceptos:**

- Rutas (`@app.get`, `@app.post`), validación con Pydantic, manejo de errores.
- CORS, dependencias, y documentación Swagger.

**Práctica:**

- Implementa endpoints `/ping` y `/predict`.
- Usa `Pydantic` para definir el input del modelo (por ejemplo, datos de partido de fútbol o dataset simple tipo Iris).
- Agrega tests con `pytest`.

**Recursos:**

- [FastAPI Tutorial Oficial](https://fastapi.tiangolo.com/tutorial/first-steps/)
- [Artículo de Dorian599](https://dorian599.medium.com/fastapi-getting-started-3294efe823a0)

------

### 🔹 **SEMANA 3 — Modelado y ML Pipeline**

**Objetivo:** Entrenar y serializar un modelo básico (por ejemplo, RandomForest para predicción de goles o clasificación Iris).

**Conceptos:**

- Preprocesamiento (`pandas`, `sklearn.pipeline`).
- Entrenamiento y exportación con `joblib` o `pickle`.
- Cargar modelo desde disco en FastAPI.

**Práctica:**

- Crea `train_model.py` que entrene y guarde `model.joblib`.
- En `model.py`, crea función `load_model()` y `predict(input_data)`.

------

### 🔹 **SEMANA 4 — Dockerización del Modelo**

**Objetivo:** Contenerizar el modelo y servirlo con FastAPI.

**Conceptos:**

- Optimizar imágenes Docker (multistage builds, `.dockerignore`).
- Variables de entorno y configuración (`.env`, `pydantic.BaseSettings`).

**Práctica:**

- Actualiza el `Dockerfile` para incluir modelo preentrenado.

- Prueba levantar el contenedor con:

  ```
  docker build -t ml-api .
  docker run -p 8000:8000 ml-api
  ```

- Valida que tu API funcione en `http://localhost:8000/docs`.

------

### 🔹 **SEMANA 5 — Testing, Logging y CI/CD local**

**Objetivo:** Darle nivel profesional al proyecto.

**Conceptos:**

- Logs estructurados (con `logging` o `loguru`).
- Testing automático con `pytest` y `requests`.
- Integración con GitHub Actions (workflow básico de CI).

**Práctica:**

- Agrega tests unitarios y de integración (API endpoints).
- Añade un `README` con badges de CI y comandos de uso.

------

### 🔹 **SEMANA 6 — MLOps / Deployment**

**Objetivo:** Preparar despliegue reproducible.

**Conceptos:**

- Diferencias entre desarrollo, staging y producción.
- Build & push a DockerHub o GitHub Container Registry.
- Introducción a FastAPI + uvicorn + nginx si quieres escalar.

**Práctica:**

- Sube tu imagen a DockerHub.
- Documenta comandos de despliegue (`docker pull`, `docker run`).
- (Opcional) Despliegue en **Render**, **Railway** o **AWS Lightsail** gratis.

------

### 🔹 **SEMANA 7 — Spark y Databricks**

**Objetivo:** Enfocar tu perfil hacia Data Engineer puro.

**Curso sugerido:**
👉 [Databricks & PySpark de 0 a Experto (Udemy)](https://www.udemy.com/course/databricks-y-apache-spark-para-big-data-de-cero-a-experto/)

**Práctica:**

- Aprende a leer datasets desde S3 o Azure Blob con PySpark.
- Haz una limpieza simple y guarda resultados en Parquet.
- Integra ese pipeline como paso previo al entrenamiento del modelo.

------

### 🔹 **SEMANA 8 — Airflow & Pipeline Completo**

**Objetivo:** Orquestar todo el flujo como haría un Data Engineer/MLOps Engineer.

**Conceptos:**

- DAGs, Operators, Tasks.
- Programar un DAG que ejecute:
  1. Ingesta de datos (Spark).
  2. Entrenamiento (Python script).
  3. Despliegue del modelo (Docker o API update).

**Recursos:**

- [Airflow Fundamentals](https://airflow.apache.org/docs/apache-airflow/stable/tutorial/fundamentals.html)
- [Guía completa en Medium](https://medium.com/@elmahfoudradwane/apache-airflow-a-complete-guide-d2e5e5dc23b0)

------

## 🎯 **3. Entrega Final / Portfolio**

Crea un **repositorio GitHub profesional** con:

- `README.md` con descripción clara, capturas del `/docs`, y arquitectura (imagen).
- Link a DockerHub o despliegue online.
- Sección “Stack utilizado” y “Lecciones aprendidas”.

Ejemplo de estructura:

```
# 🚀 ML Model API with FastAPI & Docker
Este proyecto sirve un modelo de ML (RandomForest) a través de FastAPI, totalmente dockerizado.

## Stack
- FastAPI
- Docker
- uv
- scikit-learn
- pytest
- CI/CD con GitHub Actions

## Demo
[http://yourapp.onrender.com/docs]
```

------

## 💼 **4. Extra: Preparación para Entrevistas**

- Prepara storytelling: cómo tu experiencia en Huawei + este proyecto muestra tu **capacidad de construir pipelines productivos, no solo notebooks**.
- Ten a mano métricas o diagramas (p. ej., flujo desde ingestión → entrenamiento → API).
- Explica cómo escalarías esto en la nube (AWS ECS o Azure Container Apps).



# 🗓️ PLAN DIARIO DE 8 SEMANAS — “PROYECTO DATA ENGINEER / MLOPS DEMO”

------

## **🔹 Semana 1 — Setup moderno: entorno, uv y Docker**

🎯 **Objetivo:** Entender `uv`, crear un entorno limpio y contenedor base.

### Día 1

- Instala `uv` siguiendo la [guía oficial](https://docs.astral.sh/uv/pip/environments/#using-a-virtual-environment).

- Crea tu entorno:

  ```
  uv venv
  source .venv/bin/activate
  uv pip install fastapi uvicorn pandas scikit-learn joblib
  ```

- Verifica dependencias:

  ```
  uv pip list
  ```

### Día 2

- Crea estructura de proyecto:

  ```
  ml_api_project/
  ├── app/
  │   ├── main.py
  │   ├── model.py
  │   └── utils.py
  ├── requirements.txt
  ├── Dockerfile
  └── README.md
  ```

- Añade `fastapi` mínima en `app/main.py`:

  ```
  from fastapi import FastAPI
  
  app = FastAPI()
  
  @app.get("/ping")
  def ping():
      return {"message": "pong"}
  ```

### Día 3

- Prueba local:

  ```
  uvicorn app.main:app --reload
  ```

- Comprueba en `http://localhost:8000/docs`.

### Día 4

- Aprende Docker: lee este artículo → [A Comprehensive Guide to Docker](https://medium.com/@moraneus/a-comprehensive-guide-to-docker-286d6f3ad122).

- Crea `Dockerfile`:

  ```
  FROM python:3.11-slim
  WORKDIR /app
  COPY . .
  RUN pip install fastapi uvicorn
  CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
  ```

### Día 5

- Construye y ejecuta:

  ```
  docker build -t fastapi-demo .
  docker run -p 8000:8000 fastapi-demo
  ```

- ✅ **Entrega:** API básica corriendo en Docker.

------

## **🔹 Semana 2 — FastAPI a fondo**

🎯 **Objetivo:** Construir endpoints `/predict` y validar input con Pydantic.

### Día 1

- Lee el [tutorial oficial de FastAPI](https://fastapi.tiangolo.com/tutorial/first-steps/).

- Añade `pydantic` y define input:

  ```
  from pydantic import BaseModel
  
  class MatchData(BaseModel):
      home_team_goals: int
      away_team_goals: int
      possession: float
  ```

### Día 2

- Crea endpoint `/predict` (mock):

  ```
  @app.post("/predict")
  def predict(data: MatchData):
      result = data.home_team_goals + data.away_team_goals
      return {"prediction": result}
  ```

### Día 3

- Añade manejo de errores (HTTPException).

- Testea con `curl` o Postman:

  ```
  curl -X POST http://localhost:8000/predict -H "Content-Type: application/json" -d '{"home_team_goals":1, "away_team_goals":2, "possession":60.5}'
  ```

### Día 4

- Añade documentación personalizada (`description`, `summary` en endpoints).
- Revisa `/redoc`.

### Día 5

- ✅ **Entrega:** API funcional con validación y mock de predicción.

------

## **🔹 Semana 3 — Entrenamiento ML y pipeline**

🎯 **Objetivo:** Entrenar un modelo simple y cargarlo en FastAPI.

### Día 1

- Usa `scikit-learn` con dataset `iris`:

  ```
  from sklearn.datasets import load_iris
  from sklearn.model_selection import train_test_split
  from sklearn.ensemble import RandomForestClassifier
  import joblib
  ```

### Día 2

- Crea `train_model.py`:

  ```
  iris = load_iris()
  X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, random_state=42)
  clf = RandomForestClassifier()
  clf.fit(X_train, y_train)
  joblib.dump(clf, "model.joblib")
  ```

### Día 3

- En `app/model.py`, añade:

  ```
  import joblib
  model = joblib.load("model.joblib")
  
  def predict(features):
      return model.predict([features]).tolist()
  ```

### Día 4

- Modifica tu endpoint `/predict` para usar el modelo:

  ```
  @app.post("/predict")
  def predict(data: MatchData):
      pred = predict([data.home_team_goals, data.away_team_goals, data.possession])
      return {"prediction": pred}
  ```

### Día 5

- ✅ **Entrega:** modelo ML funcional, cargado en FastAPI.

------

## **🔹 Semana 4 — Dockerización completa**

🎯 **Objetivo:** Servir el modelo en contenedor reproducible.

### Día 1–2

- Actualiza tu `Dockerfile`:

  ```
  FROM python:3.11-slim
  WORKDIR /app
  COPY . .
  RUN pip install -r requirements.txt
  CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
  ```

### Día 3

- Crea `.dockerignore`:

  ```
  __pycache__
  *.pyc
  .venv
  .git
  ```

- Build y run:

  ```
  docker build -t ml-api .
  docker run -p 8000:8000 ml-api
  ```

### Día 4–5

- ✅ **Entrega:** imagen Docker con modelo embebido lista para subir a DockerHub.

------

## **🔹 Semana 5 — Testing, Logging y CI/CD**

🎯 **Objetivo:** Añadir profesionalismo y calidad.

### Día 1

- Instala `pytest` y crea `tests/test_api.py`.

  ```
  from fastapi.testclient import TestClient
  from app.main import app
  
  client = TestClient(app)
  
  def test_ping():
      response = client.get("/ping")
      assert response.status_code == 200
  ```

### Día 2–3

- Añade logs con `logging`:

  ```
  import logging
  logging.basicConfig(level=logging.INFO)
  logger = logging.getLogger(__name__)
  ```

### Día 4

- Crea pipeline CI básico en `.github/workflows/test.yml`.

### Día 5

- ✅ **Entrega:** tests + CI funcional.

------

## **🔹 Semana 6 — Deployment y MLOps**

🎯 **Objetivo:** Publicar tu API en la nube.

### Día 1–2

- Crea cuenta en **DockerHub**.

  ```
  docker tag ml-api <usuario>/ml-api:latest
  docker push <usuario>/ml-api:latest
  ```

### Día 3–4

- Despliega en **Render** o **Railway**.
  (Render: selecciona “Deploy Docker” y conecta tu repo).

### Día 5

- ✅ **Entrega:** link público a tu API online.

------

## **🔹 Semana 7 — Spark / Databricks**

🎯 **Objetivo:** Ampliar hacia ingeniería de datos.

### Día 1–2

- Inicia curso de [Databricks y PySpark](https://www.udemy.com/course/databricks-y-apache-spark-para-big-data-de-cero-a-experto/).

- Instala PySpark localmente:

  ```
  uv pip install pyspark
  ```

### Día 3–4

- Crea mini pipeline Spark:

  ```
  from pyspark.sql import SparkSession
  spark = SparkSession.builder.appName("demo").getOrCreate()
  df = spark.read.csv("data.csv", header=True, inferSchema=True)
  df.write.parquet("output/")
  ```

### Día 5

- ✅ **Entrega:** pipeline Spark que limpia y guarda datos en Parquet.

------

## **🔹 Semana 8 — Airflow & Orquestación**

🎯 **Objetivo:** Crear pipeline orquestado tipo producción.

### Día 1

- Instala Airflow (versión local o Docker Compose).
  [Airflow Quickstart](https://airflow.apache.org/docs/apache-airflow/stable/start.html)

### Día 2–3

- Crea DAG con tres tareas:
  1. Ingesta (Spark script)
  2. Entrenamiento (Python)
  3. Despliegue (Docker build)

### Día 4

- Programa DAG diario con `schedule_interval='@daily'`.

### Día 5

- ✅ **Entrega:** DAG funcional y documentado.

------

## 🎯 RESULTADO FINAL

Al final tendrás:
✅ **Repositorio GitHub profesional**
✅ **Imagen Docker publicada**
✅ **API pública online**
✅ **Pipeline Spark + Airflow (opcional)**
✅ **Historial de commits demostrable**