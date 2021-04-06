from fastapi import FastAPI
from data import Data

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/name")
def name():
    data = Data.name()
    return {'data' : data}

@app.get("/tennis")
def tennis():
    data = Data.tennis()
    return {'data' : data}