from fastapi import FastAPI
from fastapi.datastructures import UploadFile 
from fastapi import File
import predict


app = FastAPI()

@app.get('/')
def welcome():
    return "Welcome to Paddy Disease Classification"

@app.post('/api/predict')
def prediction(file: bytes = File(...)):
    image = predict.read_image(file)
    result = predict.predict_image(image)
    return result

