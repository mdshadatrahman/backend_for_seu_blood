from fastapi import Depends, FastAPI, APIRouter, Response, status, HTTPException
from typing import List
from sqlalchemy.orm import Session

from app import models
from .database import get_db
from . import schemas

router = APIRouter(
    prefix="/requests",
    tags=["Requests"]
)


@router.get("/", response_model=List[schemas.BloodRequest])
def get_all_requests(db: Session = Depends(get_db)):
    all_requests = db.query(models.BloodRequest).all()
    return all_requests
