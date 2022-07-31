from datetime import datetime


from datetime import datetime
from pydantic import BaseModel


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
