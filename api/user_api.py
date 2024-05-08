from fastapi import APIRouter
from user_dto import UserDto
from database.userservice import *

user = APIRouter(prefix="/user")


@user.post("/registration")
def registration(user_model: UserDto):
    print(f"{user_model} Hello ")
    user_data = dict(user_model)
    print(user_data["phone_number"])
    phone_number = check_phone_number(user_data["phone_number"])
    print(f"{phone_number} =================================================")
    if phone_number == True:
        reg_user = registration(**user_data)
        return {"status": 1, "message": "Successfully registered"}
    else:
        return {"status": 0, "message": phone_number}
