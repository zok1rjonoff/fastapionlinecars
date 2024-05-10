from database import get_db
import re
from models.models import User
from datetime import datetime


def registration_db(name, phone_number, password, is_admin=False):
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
        if phone_number:
            return f"This {phone_number} phone number exist"
        else:
            return True
    else:
        return "Something wrong with this phone number "


def make_admin_by_phone_number_db(phone_number):
    print(phone_number)
    exist = db.query(User).filter_by(phone_number=phone_number).first()
    if exist:
        exist.is_admin = True
        db.commit()
        return True
    else:
        return False


def make_admin_by_id_db(user_id):
    print(user_id)
    db = next(get_db())
    exist = db.query(User).filter_by(id=user_id).first()
    print(exist)
    if exist:
        exist.is_admin = True
        db.commit()
        return True
    else:
        return False


def delete_user_by_phone_number_db(phone_number):
    db = next(get_db())
    exist = db.query(User).filter_by(phone_number=phone_number).first()
    if exist:
        db.delete(exist)
        db.commit()
        return True
    else:
        return False


def delete_user_by_id_db(user_id):
    db = next(get_db())
    exist = db.query(User).filter_by(user_id=user_id).first()
    if exist:
        db.delete(exist)
        db.commit()
        return True
    else:
        return False


def change_user_info_db(user_id, changeable_info, new_data):
    db = next(get_db())
    user = db.query(User).filter_by(id=user_id).first()
    if user:
        if changeable_info == "name":
            user.name = new_data
            db.commit()
            return True
        elif changeable_info == "phone_number":
            user.phone_number = new_data
            db.commit()
            return True
        elif changeable_info == "password":
            user.password = new_data
            db.commit()
            return True
    else:
        return False


def get_all_user_from_db():
    return next(get_db()).query(User).all()


def get_user_by_id_db(id):
    user = next(get_db()).query(User).filter_by(id=id).first()
    return user if user else "Not found"


def get_user_by_phone_number_db(phone_number):
    user = next(get_db()).query(User).filter_by(phone_number=phone_number).first()
    return user if user else "Not found"


def delete_admin_by_phone_number_db(phone_number):
    db = next(get_db())
    exist = db.query(User).filter_by(phone_number=phone_number).first()
    if exist:
        exist.is_admin = False
        db.commit()
        return True
    else:
        return False


def delete_admin_by_id_db(id):
    db = next(get_db())
    exist = db.query(User).filter_by(id=id).first()
    if exist:
        exist.is_admin = False
        db.commit()
        return True
    else:
        return False