from fastapi import APIRouter, Depends, HTTPException, status
from . import schemas
from sqlalchemy.orm import Session
from . import database
from . import models
from . import utils

router = APIRouter(
    prefix="/auth",
    tags=["Authentications"]
)


@router.post("/register", status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)
def register_user(user: schemas.BaseUser, db: Session = Depends(database.get_db)):
    user_email_query = db.query(models.Users).filter(
        models.Users.email == user.email).first()

    user_phone_query = db.query(models.Users).filter(
        models.Users.email == user.email).first()

    if user_phone_query:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail=f"User with the same email already exists")

    if user_email_query:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail=f"User with the same email already exists")

    hashed_password = utils.hash(user.password)
    user.password = hashed_password

    new_user = models.Users(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user
