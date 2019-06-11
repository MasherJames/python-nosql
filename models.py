import os
from mongoengine import *

connect(db=os.getenv("DB"), host=os.getenv("HOST"), port=os.getenv("PORT"))

class User(Document):
    email = EmailField(required=True)
    username = StringField(required=True, max_length=50)
    password = StringField(required=True, max_length=50)

class TenantsReviews(EmbeddedDocument):
    content = StringField()

class Apartment(Document):
    name = StringField(required=True, max_length=50)
    number_of_rooms = IntField(required=True)
    location = StringField(required=True, max_length=50)
    rent_per_month = IntField(required=True)
    tags = ListField(StringField(max_length=30))
    tenants_reviews = ListField(EmbeddedDocumentField(TenantsReviews))

    meta = {'allow_inheritance':True}

class ApartmentImg(Apartment):
    img_path = StringField()
