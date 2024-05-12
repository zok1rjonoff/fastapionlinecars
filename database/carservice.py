from database import get_db
from models.models import Cars, Manufacturer, User, CarComment
from datetime import datetime
from dto.user_dto import CarDto, CommentDto


def get_all_cars_db():
    db = next(get_db())
    cars = db.query(Cars).all()
    car_dtos = []

    for car in cars:
        owner = db.query(User).filter(User.id == car.car_owner_id).first()
        manufacturer = db.query(Manufacturer).filter(Manufacturer.id == car.manufacturer_id).first()
        car_comments = db.query(CarComment).filter(CarComment.car_id == car.id).all()

        comment_dtos = []
        for comment in car_comments:
            user_name = db.query(User).filter(User.id == comment.user_id).first().name
            comment_dtos.append(CommentDto(
                user_id=comment.user_id,
                user_name=user_name,
                comment=comment.comment,
                created_at=comment.created_at
            ))

        car_dto = CarDto(
            car_id=car.id,
            car_owner_name=owner.name,
            car_owner_phone_number=owner.phone_number,
            car_owner_id=car.car_owner_id,
            car_manufacturer_id=car.manufacturer_id,
            car_manufacturer=manufacturer.manufacturer_name,
            car_name=car.car_name,
            car_year=car.car_year,
            car_description=car.car_description,
            car_km=car.car_km,
            car_fuel=car.car_fuel,
            car_gearbox=car.car_gearbox,
            car_color=car.car_color,
            car_price=car.car_price,
            made_in=car.made_in,
            car_image=car.car_image,
            car_comments=comment_dtos,
            created_at=car.car_created_at
        )

        car_dtos.append(car_dto)

    return car_dtos


def add_car_db(manufacturer_id, owner_id, car_name, car_year, car_description, car_km,
               car_fuel, car_gearbox, car_color, car_price, made_in, car_image_url):
    db = next(get_db())
    manufacturer_id_db = db.query(Manufacturer).filter_by(id=manufacturer_id).first().id
    owner_id_db = db.query(User).filter_by(id=owner_id).first().id
    if manufacturer_id_db:
        if owner_id_db:
            new_car = Cars(
                manufacturer_id=manufacturer_id,
                car_owner_id=owner_id,
                car_name=car_name,
                car_year=car_year,
                car_description=car_description,
                car_km=car_km,
                car_fuel=car_fuel,
                car_gearbox=car_gearbox,
                car_color=car_color,
                car_price=car_price,
                made_in=made_in,
                car_image=car_image_url,
                car_created_at=datetime.now()
            )
            db.add(new_car)
            db.commit()
            return "Added"
        else:
            return "User do not exist"
    else:
        return "Manufacturer not found"


def get_car_by_id_db(car_id: int):
    db = next(get_db())
    car = db.query(Cars).filter(Cars.id == car_id).first()
    if car is None:
        return None

    owner = db.query(User).filter(User.id == car.car_owner_id).first()
    manufacturer = db.query(Manufacturer).filter(Manufacturer.id == car.manufacturer_id).first()
    car_comments = db.query(CarComment).filter(CarComment.car_id == car.id).all()

    comment_dtos = []
    for comment in car_comments:
        user_name = db.query(User).filter(User.id == comment.user_id).first().name
        comment_dtos.append(
            CommentDto(user_id=comment.user_id, user_name=user_name, comment=comment.comment,
                       created_at=comment.created_at))

    car_dto = CarDto(
        car_id=car.id,
        car_owner_id=car.car_owner_id,
        car_owner_name=owner.name,
        car_owner_phone_number=owner.phone_number,
        car_manufacturer_id=car.manufacturer_id,
        car_manufacturer=manufacturer.manufacturer_name,
        car_name=car.car_name,
        car_year=car.car_year,
        car_description=car.car_description,
        car_km=car.car_km,
        car_fuel=car.car_fuel,
        car_gearbox=car.car_gearbox,
        car_color=car.car_color,
        car_price=car.car_price,
        made_in=car.made_in,
        car_image=car.car_image,
        car_comments=comment_dtos,
        created_at=car.car_created_at
    )

    return car_dto


def get_cars_by_user_id_db(user_id: int):
    db = next(get_db())
    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        return "User not found"

    cars = db.query(Cars).filter(Cars.car_owner_id == user_id).all()
    car_dtos = []

    for car in cars:
        manufacturer = db.query(Manufacturer).filter(Manufacturer.id == car.manufacturer_id).first()
        car_comments = db.query(CarComment).filter(CarComment.car_id == car.id).all()

        comment_dtos = []
        for comment in car_comments:
            user_name = db.query(User).filter(User.id == comment.user_id).first().name
            comment_dtos.append(CommentDto(
                user_id=comment.user_id,
                user_name=user_name,
                comment=comment.comment,
                created_at=comment.created_at
            ))

        car_dto = CarDto(
            car_id=car.id,
            car_owner_id=car.car_owner_id,
            car_owner_name=user.name,
            car_owner_phone_number=user.phone_number,
            car_manufacturer_id=car.manufacturer_id,
            car_manufacturer=manufacturer.manufacturer_name,
            car_name=car.car_name,
            car_year=car.car_year,
            car_description=car.car_description,
            car_km=car.car_km,
            car_fuel=car.car_fuel,
            car_gearbox=car.car_gearbox,
            car_color=car.car_color,
            car_price=car.car_price,
            made_in=car.made_in,
            car_image=car.car_image,
            car_comments=comment_dtos,
            created_at=car.car_created_at
        )

        car_dtos.append(car_dto)

    return car_dtos


def delete_car_by_id_db(car_id):
    db = next(get_db())
    exist = db.query(Cars).filter_by(id=car_id).first()
    if exist:
        db.delete(exist)
        db.commit()
        return True
    return False
