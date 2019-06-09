from flask import Flask
from flask_restful import Api

from .views.apartment import ApartmentView

def app_factory(config_mode):
    app = Flask(__name__)
    api = Api(app)

    api.add_resource(ApartmentView, "/api/apartments")
    return app