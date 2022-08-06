from fastapi import APIRouter, Depends, HTTPException, status
import oauth2
import schemas
from sqlalchemy.orm import Session
import database
import models
import utils
from fastapi.security.oauth2 import OAuth2PasswordRequestForm

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


@router.post('/login', response_model=schemas.Token)
def login(user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    user = db.query(models.Users).filter(
        models.Users.email == user_credentials.username).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid credentials")

    if not utils.verify(user_credentials.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid credentials")

    access_token = oauth2.create_access_token(data={"user_id": user.id})

    return {"access_token": access_token, "token_type": "bearer"}
