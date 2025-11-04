# 🚀 ML Model API — FastAPI + Docker + uv + MLOps

![Python](https://img.shields.io/badge/Python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![Docker](https://img.shields.io/badge/Docker-Containerization-blue)
![CI/CD](https://img.shields.io/badge/GitHub%20Actions-CI%2FCD-yellow)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

---

## 🧠 Descripción del Proyecto

Este proyecto implementa un **modelo de Machine Learning** servido mediante una **API REST construida con FastAPI**, gestionada con `uv` y totalmente **dockerizada**.  
Está pensado como una **demo de MLOps/Data Engineering** para entrevistas técnicas y portfolio profesional.

El flujo completo incluye:
1. Entrenamiento del modelo (`scikit-learn`).
2. Serialización con `joblib`.
3. Servicio de inferencia vía FastAPI.
4. Empaquetado en contenedor Docker.
5. (Opcional) Orquestación con **Airflow** y preprocesamiento en **PySpark**.

---

## 🧩 Stack Tecnológico

| Componente | Tecnología / Herramienta | Propósito |
|-------------|--------------------------|------------|
| Lenguaje | **Python 3.11** | Base del proyecto |
| Framework API | **FastAPI** | Exposición del modelo vía REST |
| ML | **scikit-learn**, **pandas**, **joblib** | Entrenamiento y predicción |
| Entorno | **uv** | Gestión ligera y rápida de entornos virtuales |
| Contenerización | **Docker** | Despliegue reproducible |
| Testing | **pytest** | Tests unitarios e integración |
| CI/CD | **GitHub Actions** | Automatización de pruebas y builds |
| Data Engineering | **PySpark**, **Databricks** | Procesamiento de datos a gran escala |
| Orquestación | **Apache Airflow** | Pipeline productivo (MLOps avanzado) |

---
