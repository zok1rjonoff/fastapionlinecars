from datetime import datetime
from typing import List

from pydantic import BaseModel


class UserDto(BaseModel):
    id: int
    name: str
    phone_number: str
    password: str
    is_admin: bool
    created_at: datetime


class CommentDto(BaseModel):
    user_id: int
    user_name: str
    comment: str
    created_at: datetime


class CarDto(BaseModel):
    car_id: int
    car_owner_id: int
    car_owner_name: str
    car_owner_phone_number: str
    car_manufacturer_id: int
    car_manufacturer: str
    car_name: str
    car_year: int
    car_description: str
    car_km: int
    car_fuel: str
    car_gearbox: str
    car_color: str
    car_price: float
    made_in: str
    car_image: str
    car_comments: List[CommentDto]
    created_at: datetime
