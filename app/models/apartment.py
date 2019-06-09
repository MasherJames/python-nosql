import os
from mongoengine import *
from flask import current_app

connect(db=os.getenv("db"), username=os.getenv("username"), host=os.getenv("host"), password=os.getenv("password"), port=int(os.getenv("port")))

class Apartment(Document):
    name = StringField(required=True, max_length=50)
    number_of_rooms = IntField(required=True)
    location = StringField(required=True, max_length=50)
    rent_per_month = IntField(required=True)

