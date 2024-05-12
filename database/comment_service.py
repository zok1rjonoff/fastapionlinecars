from datetime import datetime
from database import get_db
from models.models import *


def add_comment_db(user_id, car_id, comment):
    db = next(get_db())
    user = db.query(User).filter_by(id=user_id).first()
    car = db.query(Cars).filter_by(id=car_id).first()
    if user:
        if car:
            new_comment = CarComment(user_id=user_id, car_id=car_id, comment=comment, created_at=datetime.now())
            db.add(new_comment)
            db.commit()
            return True
        else:
            return "Car not found"
    return "User not found"


def get_user_comments_db(user_id):
    db = next(get_db())
    user = db.query(User).filter_by(id=user_id).first()
    comments = db.query(CarComment).filter(CarComment.user_id == user_id).all()
    if comments:
        user_comments = [{
            "user_id": user.id,
            "user_name": user.name,
            "car_id": comment.car_id,
            "car_name": db.query(Cars).filter(Cars.id == comment.car_id).first().car_name,
            "comment": comment.comment,
            "created_at": comment.created_at
        } for comment in comments]

        return user_comments
    else:
        return "No comments found for this user."


def get_car_comments_db(car_id):
    db = next(get_db())
    comment = db.query(CarComment).filter(CarComment.car_id == car_id).all()
    if comment:
        car_comment = [{
            "car_id": car.car_id,
            "car_name": db.query(Cars).filter_by(id=car_id).first().car_name,
            "user_id": car.user_id,
            "user_name": db.query(User).filter_by(id=car.user_id).first().phone_number,
            "comments": car.comment,
            "created_at": car.created_at
        } for car in comment]
        return car_comment
    else:
        return "Not found"
