from sqlalchemy import TIMESTAMP, Boolean, Column, Integer, String, text
from database import Base


class BloodRequest(Base):
    __tablename__ = 'blood_request'
    id = Column(Integer, primary_key=True, nullable=False)
    posted_by = Column(String, nullable=False)
    donation_time = Column(TIMESTAMP(timezone=True), nullable=False)
    blood_group = Column(String, nullable=False)
    bag_needed = Column(Integer, nullable=False)
    blood_type = Column(String, nullable=False)
    hospital_name = Column(String, nullable=False)
    contact_number = Column(String, nullable=False)
    urgent = Column(Boolean, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        server_default=text("NOW()"), nullable=False)


class Users(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    phone_number = Column(String, nullable=False, unique=True)
    full_name = Column(String, nullable=False)
    blood_group = Column(String, nullable=False)
    dob = Column(String, nullable=False, server_default="notset")
    department = Column(String, nullable=False, server_default="notset")
    address = Column(String, nullable=False, server_default="notset")
    last_donation = Column(String, nullable=False,
                           server_default="notset")
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text("NOW()"))
