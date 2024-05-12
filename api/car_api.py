from fastapi import APIRouter, UploadFile, File
from database.carservice import *
from datetime import datetime, time, date

car = APIRouter(prefix="/car")


@car.get("/get-all-cars")
async def get_all_cars():
    return {"status": 1, "message": get_all_cars_db()}


@car.post("/add-car")
async def add_car(manufacturer_id, owner_id, car_name, car_year,
                  car_description, car_km, car_fuel, car_gearbox, car_color, car_price, made_in,
                  car_image: UploadFile = File(...)):
    print(car_image.filename)
    if car_image:
        with open(f"database/car_images/{car_image.filename}.jpg", "wb") as photo:

            photo_to_save = await car_image.read()
            result = add_car_db(manufacturer_id, owner_id, car_name, car_year, car_description, car_km, car_fuel,
                                car_gearbox, car_color, car_price, made_in,
                                f"database/car_images/{car_image.filename}.jpg")
            if result == "Added":
                photo.write(photo_to_save)
                return {"status": 1, "message": "Car added successfully"}
            else:
                return {"status": 0, "message": result}

    return {"status": 0, "message": "Wrong image"}


@car.get("/get-car-by-id")
def get_car_by_id(id):
    return {"status": 1, "message": get_car_by_id_db(id)}


@car.get("/get-car-by-user-id")
def get_car_by_user_id(user_id):
    res = get_cars_by_user_id_db(user_id)
    if res != "Not Found":
        return {"status": 1, "message": res}
    return {"status": 0, "message": res}


@car.delete("/delete-car-by-id")
def delete_car_by_id(car_id):
    if delete_car_by_id_db(car_id):
        return {"status": 1, "message": "Deleted"}
    return {"status": 0, "message": "Car not found"}
