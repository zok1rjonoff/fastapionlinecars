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
        reg_user = registration_db(**user_data)
        return {"status": 1, "message": "Successfully registered"}
    else:
        return {"status": 0, "message": phone_number}


@user.get("/get-all-users")
def get_all_users():
    return {"status": 1, "message": get_all_user_from_db()}


@user.get("/get-user-by-id")
def get_user_by_id(id):
    return {"status": 1, "message": get_user_by_id_db(id) if get_user_by_id_db(id) else "Not found"}


@user.get("/get-user-by-phone-number")
def get_by_phone_number(phone_number):
    return {"status": 1, "message": get_user_by_phone_number_db(phone_number) if get_user_by_phone_number_db(
        phone_number) else "Not found"}


@user.put("/make-admin-by-phone_number")
def make_admin_phone(phone_number):
    print(phone_number)
    if make_admin_by_phone_number_db(phone_number):
        return {"status": 1, "message": "Done"}
    else:
        return {"status": 0, "message": "Something went wrong "}


@user.put("/make-admin-by-id")
def make_admin_id(id):
    if make_admin_by_id_db(id):
        return {"status": 1, "message": "Done"}
    else:
        return {"status": 0, "message": "Something went wrong "}


@user.put("/delete-admin-by-phone_number")
def delete_admin_by_phone_number(phone_number):
    if delete_admin_by_phone_number_db(phone_number):
        return {"status": 1, "message": "Done"}
    else:
        return {"status": 0, "message": "Something went wrong"}


@user.put("/delete-admin-by-id")
def delete_admin_by_id(id):
    print(id)
    print(type(id))
    if delete_admin_by_id_db(id):
        return {"status": 1, "message": "Done"}
    else:
        return {"status": 0, "message": "Something went wrong"}


@user.put("/change-user-info")
def change_user_info(id, changeable_info, new_data):
    if change_user_info_db(id, changeable_info, new_data):
        return {"status": 1, "message": "Updated successfully"}
    else:
        return {"status": 0, "message": "Something went wrong"}


@user.delete("/delete-user-by-id")
def delete_user_by_id(id):
    if delete_user_by_id_db(id):
        return {"status": 1, "message": "Deleted"}
    else:
        return {"status": 0, "message": "Something went wrong"}


@user.delete("/delete-user-by-phone_number")
def delete_user_by_phone_number(phone_number):
    if delete_user_by_phone_number_db(phone_number):
        return {"status": 1, "message": "Deleted"}
    else:
        return {"status": 0, "message": "Something went wrong"}
