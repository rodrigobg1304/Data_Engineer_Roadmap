#!/bin/bash
# ==============================================================
# 🚀 setup.sh — Script para crear entorno y levantar API ML con FastAPI + uv
# Compatible con macOS / Linux
# ==============================================================

PROJECT_NAME="ml_api_project"

echo "📦 Creando proyecto: $PROJECT_NAME"
mkdir -p $PROJECT_NAME/app
cd $PROJECT_NAME || exit

# --------------------------------------------------------------
# 1️⃣ Verificar instalación de uv
# --------------------------------------------------------------
if ! command -v uv &> /dev/null
then
    echo "⚠️  uv no está instalado. Instalando ahora..."
    curl -LsSf https://astral.sh/uv/install.sh | sh
    export PATH="$HOME/.local/bin:$PATH"
else
    echo "✅ uv encontrado."
fi

# --------------------------------------------------------------
# 2️⃣ Crear entorno virtual con uv
# --------------------------------------------------------------
echo "🧩 Creando entorno virtual..."
uv venv
source .venv/bin/activate

# --------------------------------------------------------------
# 3️⃣ Instalar dependencias
# --------------------------------------------------------------
echo "📚 Instalando dependencias..."
uv pip install fastapi uvicorn pandas scikit-learn joblib pytest

# --------------------------------------------------------------
# 4️⃣ Crear estructura de archivos base
# --------------------------------------------------------------
echo "🧱 Creando estructura de proyecto..."

# app/__init__.py
echo "" > app/__init__.py

# app/main.py
cat << 'EOF' > app/main.py
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="ML Model API",
    description="API para servir un modelo de Machine Learning",
    version="0.1.0",
)

@app.get("/")
def root():
    return {"message": "Hello World! 🌍"}

@app.get("/ping")
def ping():
    return {"message": "pong 🏓"}

EOF

# app/model.py
cat << 'EOF' > app/model.py
EOF

# app/utils.py
cat << 'EOF' > app/utils.py
EOF

# requirements.txt
echo "fastapi
uvicorn
pandas
scikit-learn
joblib
pytest" > requirements.txt

# .dockerignore
echo "__pycache__/
.venv/
*.pyc
.git/" > .dockerignore

# Dockerfile
cat << 'EOF' > Dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
EOF

echo "🧱 Proyecto construido"