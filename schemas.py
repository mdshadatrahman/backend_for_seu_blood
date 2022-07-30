from datetime import datetime


from datetime import datetime
from pydantic import BaseModel


class BloodRequest(BaseModel):
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
