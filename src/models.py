from src.configuration.database import Base
from sqlalchemy import Column, Integer, String, Date

class Contact(Base):
    __tablename__ = 'contacts'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, index=True, unique=True)
    phone_number = Column(String, index=True)
    birth_date = Column(Date)
    additional_data = Column(String, nullable=True)