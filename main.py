from fastapi import FastAPI
from pydantic import BaseModel
import joblib

app = FastAPI()

# ✅ Load the trained model
model = joblib.load("iris_model.joblib")
print("✅ Model loaded successfully")

# ✅ Map numeric predictions to class names
label_map = {0: "setosa", 1: "versicolor", 2: "virginica"}

# ✅ Define input schema
class IrisFeatures(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

# ✅ Root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the Iris Classifier API!"}

# ✅ Health check endpoint
@app.get("/health")
def health_check():
    return {"status": "ok"}

# ✅ Prediction endpoint
@app.post("/predict")
def predict(features: IrisFeatures):
    data = [[
        features.sepal_length,
        features.sepal_width,
        features.petal_length,
        features.petal_width
    ]]
    prediction = model.predict(data)[0]
    class_name = label_map.get(prediction, "unknown")
    return {"prediction": class_name}