markdown
# 🌸 Iris Classifier API

A FastAPI-based machine learning API that predicts the species of an Iris flower based on its petal and sepal measurements. This project is part of the Intelligent Systems assignment.

---

## 📁 Project Structure

iris_classifier/ ├── iris_model.pkl # Trained ML model (scikit-learn) ├── main.py # FastAPI app with prediction endpoint ├── README.md # Project documentation

Code

---

## 🚀 How to Run the API

### 1. Install Dependencies

```bash
pip install fastapi uvicorn scikit-learn
2. Start the Server
bash
uvicorn main:app --reload
The API will be available at: http://127.0.0.1:8000

🔍 API Endpoint
POST /predict
Request Body (JSON):

json
{
  "sepal_length": 5.1,
  "sepal_width": 3.5,
  "petal_length": 1.4,
  "petal_width": 0.2
}
Response:

json
{
  "prediction": "Iris-setosa"
}
🧠 Model Details
Algorithm: Logistic Regression

Dataset: Iris dataset from scikit-learn

Features: Sepal length, sepal width, petal length, petal width

Target: Iris species (setosa, versicolor, virginica)

📦 Packaging for Submission
To submit this project:

Ensure the following files are present:

main.py

iris_model.pkl

README.md

Zip the folder:

bash
zip -r iris_classifier.zip iris_classifier/
🙋 Author
Name: Sachin Course: Intelligent Systems University ID: [Add your ID here if required]
