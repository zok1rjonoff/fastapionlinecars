from sqlalchemy import Table, Column, Integer, ForeignKey, String, Text, DateTime, Boolean, Float
from sqlalchemy.orm import relationship
from database import Base

# Define the association table for many-to-many relationship
car_comment_association = Table(
    'car_comment_association',
    Base.metadata,
    Column('car_id', Integer, ForeignKey('cars.id', ondelete="CASCADE")),
    Column('comment_id', Integer, ForeignKey('comments.id', ondelete="CASCADE"))
)


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, autoincrement=True, unique=True, nullable=False, primary_key=True)
    name = Column(String, nullable=False)
    phone_number = Column(String, unique=True)
    password = Column(String, nullable=False)
    is_admin = Column(Boolean, default=False)
    registration_date = Column(DateTime)
    # Establish one-to-many relationship with comments
    comments = relationship("CarComment", back_populates="user", cascade="all, delete-orphan")


class Manufacturer(Base):
    __tablename__ = "manufacturer"
    id = Column(Integer,autoincrement=True,primary_key=True)
    manufacturer_name = Column(String, nullable=False, unique=True)
    created_at = Column(DateTime)


class Cars(Base):
    __tablename__ = "cars"
    id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)
    manufacturer_id = Column(ForeignKey("manufacturer.id", ondelete="CASCADE"))
    car_owner_id = Column(ForeignKey('users.id', ondelete="SET NULL"))
    car_name = Column(String, nullable=False)
    car_year = Column(Integer, nullable=False)
    car_description = Column(Text, nullable=True)
    car_km = Column(Integer, nullable=False)
    car_fuel = Column(String, nullable=False)
    car_gearbox = Column(String, nullable=False)
    car_color = Column(String, nullable=False)
    car_price = Column(Float, nullable=False)
    made_in = Column(String, nullable=False)
    car_image = Column(String, nullable=False)
    car_created_at = Column(DateTime)
    # Establish one-to-many relationship with comments
    comments = relationship("CarComment", secondary=car_comment_association, back_populates="cars", cascade="all, delete-orphan")
    manufacturer_fk = relationship("CarManufacturer", lazy="subquery")
    owner_fk = relationship("User", lazy="subquery")


class CarComment(Base):
    __tablename__ = "comments"
    id = Column(Integer, autoincrement=True, primary_key=True)
    user_id = Column(ForeignKey('users.id', ondelete="CASCADE"))
    comment = Column(Text, nullable=False)
    created_at = Column(DateTime)
    # Establish one-to-many relationship with users
    user = relationship("User", back_populates="comments")
    # Establish many-to-many relationship with cars
    cars = relationship("Cars", secondary=car_comment_association, back_populates="comments")

