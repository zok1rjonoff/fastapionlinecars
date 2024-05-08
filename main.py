from fastapi import FastAPI
from database import Base, engine
from api.user_api import user
from api.manufacturer_api import manufacturer

# подключение к проекту базы данных и создание всех таблиц
Base.metadata.create_all(bind=engine)
app = FastAPI(docs_url="/")
app.include_router(user)
app.include_router(manufacturer)
