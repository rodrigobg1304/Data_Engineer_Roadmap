import kagglehub
import pandas as pd
import os

# Download latest version
path = kagglehub.dataset_download("emanfatima2025/titanic-passenger-survival-prediction-dataset")

print("Path to dataset files:", path)

# Ver qué hay en la carpeta descargada
print(os.listdir(path))

# Cargar el CSV (ajusta el nombre si es diferente)
csv_file = os.path.join(path, "tested.csv")
df = pd.read_csv(csv_file)

# Mostrar las primeras filas
print(df.head())

