from time import sleep
from fastapi import FastAPI
import psycopg2
from app import auth, blood_request
from . import models
from .database import engine
from psycopg2.extras import RealDictCursor

models.Base.metadata.create_all(bind=engine)


app = FastAPI()

app.include_router(auth.router)


while True:
    try:
        conn = psycopg2.connect(host="localhost", database="seu_blood",
                                user="postgres", password="toor", cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("connection was successful")
        break

    except Exception as error:
        print("Connection Failed")
        sleep(2)

app.include_router(blood_request.router)


@app.get("/")
def root():
    return {"Working": "I hope it is working"}
