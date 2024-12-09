from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import pymysql, sqlalchemy


# Define the connection to the MariaDB database
# DATABASE_URI = "mariadb+mariadbconnector://t1:YWQQEg1QwgVTc40K@34.125.69.91/f24_housing_db" 
username = 't2'  # Replace with actual username
password = 'vVpLVI1WJtknBJV0'  # Replace with actual password
engine = sqlalchemy.create_engine(f"mysql+pymysql://{username}:{password}@34.125.69.91/f24_housing_db", connect_args={'ssl': {'disabled': True}})
Base = declarative_base()


class UserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError("The Username field is required")
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(username, password, **extra_fields)


# SQLAlchemy ORM model mapping the user table in MariaDB
class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(150), unique=True)
    password = Column(String(150))  # Ensure this matches the hash method in use
    firstname = Column(String(100))
    lastname = Column(String(100))
    active = Column(Boolean, default=True)
    

# Create a session for the database connection
Session = sessionmaker(bind=engine)
session = Session()

class Property(Base):  # New SQLAlchemy model for Property
    __tablename__ = 'property'
    id = Column(Integer, primary_key=True, autoincrement=True)
    size_sqft = Column(Integer)
    price = Column(sqlalchemy.Numeric(10, 2)) # Using sqlalchemy.Numeric for correct decimal handling
    bedrooms = Column(Integer)
    bathrooms = Column(Integer)
    user_id = Column(Integer, sqlalchemy.ForeignKey('user.id'))  # Foreign key to User
    street_address = Column(String(255))
    city = Column(String(255))
    name = Column(String(255))

class PropertyImage(Base):  # New SQLAlchemy model for PropertyImage
    __tablename__ = 'property_images'
    id = Column(Integer, primary_key=True, autoincrement=True)
    property_id = Column(Integer, sqlalchemy.ForeignKey('property.id'))
    image_url = Column(String(255))


class Match(Base):
    __tablename__ = 'match'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, sqlalchemy.ForeignKey('user.id'))
    property_id = Column(Integer, sqlalchemy.ForeignKey('property.id'))
    timestamp = Column(sqlalchemy.DateTime)
