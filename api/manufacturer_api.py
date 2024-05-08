from fastapi import APIRouter
from database.manufacturer_service import *

manufacturer = APIRouter(prefix="/manufacturer")


@manufacturer.post("/add-manufacturer")
def add_manufacturer_api(name):
    if add_manufacturer(name):
        return {"status": 1, "message": "Added"}
    else:
        return {"status": 0, "message": "smth went wring"}


@manufacturer.get("/get-all")
def get_all():
    list_manufacturer = get_all_manufacturer()
    if list_manufacturer:
        return {"status": 1, "message": list_manufacturer}
    else:
        return {"status": 0, "message": "Empty"}


@manufacturer.get("/by_id")
def get_by_id(id):
    list_manufacturer = get_exact_manufacturer(id)
    if list_manufacturer:
        return {"status": 1, "message": list_manufacturer}
    else:
        return {"status": 0, "message": "Empty"}


@manufacturer.delete("/delete")
def get_all():
    list_manufacturer = get_all_manufacturer()
    if list_manufacturer:
        return {"status": 1, "message": list_manufacturer}
    else:
        return {"status": 0, "message": "Empty"}
