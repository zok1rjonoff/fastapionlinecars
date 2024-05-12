from fastapi import APIRouter
from database.comment_service import *

comment = APIRouter(prefix="/comments")


@comment.post("/add-comment")
def add_comment(user_id, car_id, comment_text):
    res = add_comment_db(user_id, car_id, comment_text)
    if res == True:
        return {"status": 1, "message": res}
    else:
        return {"status": 0, "message": res}


@comment.get("/get-user-comment-by-user_id")
def get_user_comment(id):
    print(id)
    res = get_user_comments_db(id)
    if res != "No comments found for this user.":
        return {"status": 1, "message": res}
    else:
        return {"status": 0, "message": "Something went error"}


@comment.get("/get-car-comment")
def get_car_comment(car_id):
    res = get_car_comments_db(car_id)
    if res != "Not found":
        return {"status": 1, "message": res}
    return {"status": 0, "message": res}
