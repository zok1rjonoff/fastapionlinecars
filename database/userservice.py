from database import get_db
import re
from models.models import User
from datetime import datetime


def registration(name, phone_number, password):
    db = next(get_db())

    new_user = User(name=name, phone_number=phone_number, password=password,
                    is_admin=False, registration_date=datetime.now())
    db.add(new_user)
    db.commit()
    return "Successfully added"


def check_phone_number(phone_number):
    db = next(get_db())
    pattern = r'^(\+998|998)\d{9}$'
    if re.match(pattern, phone_number):
        phone_number = db.query(User).filter_by(phone_number=phone_number).first()
        print(F"{phone_number} ====USERSERVICE")
        if phone_number:
            return f"This {phone_number} phone number exist"
        else:
            return True
    else:
        return "Something wrong with this phone number "


def make_admin(phone_number):
    db = next(get_db())
    exist = db.query(User).filter_by(phone_number=phone_number).first()
    if exist:
        exist.is_admin = True
        db.commit()
        return f"The user with this  {phone_number} is admin"
    else:
        return f"User with this {phone_number} is not found"


def make_admin_by_id(user_id):
    db = next(get_db())
    exist = db.query(User).filter_by(user_id=user_id).first()
    if exist:
        exist.is_admin = True
        db.commit()
        return f"The user with this  {user_id} is admin"
    else:
        return f"User with this {user_id} is not found"


def delete_user_by_phone_number(phone_number):
    db = next(get_db())
    exist = db.query(User).filter_by(phone_number=phone_number).first()
    if exist:
        db.delete(exist)
        db.commit()
        return "User is deleted"
    else:
        return "User not found"


def delete_user_ny_id(user_id):
    db = next(get_db())
    exist = db.query(User).filter_by(user_id=user_id).first()
    if exist:
        db.delete(exist)
        db.commit()
        return "User is deleted"
    else:
        return "User not found"


def change_user_info(user_id, changeable_info, new_data):
    db = next(get_db())
    user = db.query(User).filter_by(user_id=user_id).first()
    if user:
        if changeable_info == "name":
            user.name = new_data
            db.commit()
            return True
        elif changeable_info == "phone_number":
            user.phone_number = new_data
            db.commit()
            return True
    else:
        return "User not found"
