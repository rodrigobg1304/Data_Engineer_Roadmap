# app/train_model.py
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

def train_and_save_model():
    # 1. Cargar dataset de ejemplo
    iris = load_iris()
    X, y = iris.data, iris.target

    # 2. Dividir en entrenamiento y test
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # 3. Entrenar modelo RandomForest
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # 4. Guardar modelo entrenado
    joblib.dump(model, "app/model_rf.pkl")
    print("✅ Modelo entrenado y guardado en app/model_rf.pkl")

if __name__ == "__main__":
    train_and_save_model()
