from fastapi import FastAPI
from . import auth
from . import models
from .database import engine

models.Base.metadata.create_all(bind=engine)


app = FastAPI()

app.include_router(auth.router)


@app.get("/")
def root():
    return {"Working": "I hope it is working"}


#from new os