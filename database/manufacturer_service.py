from database import get_db
from models.models import Manufacturer
from datetime import datetime


def add_manufacturer(name):
    db = next(get_db())

    new_manufacturer = Manufacturer(manufacturer_name=name,created_at=datetime.now())
    db.add(new_manufacturer)
    db.commit()
    return True


def get_exact_manufacturer(id):
    db = next(get_db())
    exist = db.query(Manufacturer).filter_by(id=id).first()
    if exist:
        return exist
    else:
        return "Not found"


def get_all_manufacturer():
    db = next(get_db())
    all_manufacturer = db.query(Manufacturer).all()
    if all_manufacturer:
        return all_manufacturer
    else:
        return "Empty"


def delete_manufacturer(id):
    db = next(get_db())
    exist = db.query(Manufacturer).filter_by(id=id).first()
    if exist:
        db.delete(exist)
        db.commit()
        return "Deleted"
    else:
        return "Not found"


def edit_manufacturer_db(id,name):
    db = next(get_db())
    exist = db.query(Manufacturer).filter_by(id=id).first()
    if exist:
        exist.manufacturer_name = name
        db.commit()
        return True
    else:
        return False


