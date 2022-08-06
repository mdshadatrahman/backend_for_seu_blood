from fastapi import Depends, APIRouter, Response, status, HTTPException
from typing import List
from sqlalchemy.orm import Session

from app import models
from .database import get_db
from . import schemas

router = APIRouter(
    prefix="/requests",
    tags=["Requests"]
)


@router.get("/", response_model=List[schemas.BloodRequest], status_code=status.HTTP_200_OK)
def get_all_requests(db: Session = Depends(get_db)):
    all_requests = db.query(models.BloodRequest).all()
    return all_requests


@router.post("/", response_model=schemas.BloodRequest, status_code=status.HTTP_201_CREATED)
def create_blood_request(request: schemas.CreateBloodRequest, db: Session = Depends(get_db)):
    new_request = models.BloodRequest(**request.dict())
    db.add(new_request)
    db.commit()
    db.refresh(new_request)
    return new_request


@router.put('/{id}',  response_model=schemas.BloodRequest, status_code=status.HTTP_200_OK)
def update_blood_request(id: int, request: schemas.UpdateBloodRequest, db: Session = Depends(get_db)):
    req_query = db.query(models.BloodRequest).filter(
        models.BloodRequest.id == id)
    req = req_query.first()

    if req == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blood request with id: {id} not found")

    req_query.update(request.dict(), synchronize_session=False)
    db.commit()
    return req_query.first()


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_blood_request(id: int, db: Session = Depends(get_db)):
    req_query = db.query(models.BloodRequest).filter(
        models.BloodRequest.id == id)
    request = req_query.first()
    if request == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blood request with id: {id} not found")

    req_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
