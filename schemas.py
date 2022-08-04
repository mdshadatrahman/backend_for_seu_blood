from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr


class BaseUser(BaseModel):
    email: EmailStr
    password: str
    phone_number: str
    full_name: str
    blood_group: str
    dob: Optional[str]
    department: Optional[str]
    address: Optional[str]
    last_donation: Optional[str]

    class Config:
        orm_mode = True

class UserOut(BaseUser):
    id: int
    created_at: datetime


class BloodRequest(BaseModel):
    id: int
    posted_by: str
    donation_time: datetime
    blood_group: str
    bag_needed: int
    blood_type: str
    hospital_name: str
    contact_number: str
    urgent: bool
    created_at: datetime

    class Config:
        orm_mode = True


class CreateBloodRequest(BaseModel):
    posted_by: str
    donation_time: datetime
    blood_group: str
    bag_needed: int
    blood_type: str
    hospital_name: str
    contact_number: str
    urgent: bool

    class Config:
        orm_mode = True


class UpdateBloodRequest(BaseModel):
    donation_time: datetime
    blood_group: str
    bag_needed: int
    blood_type: str
    hospital_name: str
    contact_number: str
    urgent: bool

    class Config:
        orm_mode = True
