from flask_restful import Resource, reqparse
from ..models.apartment import Apartment

class ApartmentView(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str, required=True,
                        help='This field cannot be left blank')
    parser.add_argument('number_of_rooms', type=int, required=True,
                        help='This field cannot be left blank')
    parser.add_argument('location', type=str, required=True,
                        help='This field cannot be left blank')
    parser.add_argument('rent_per_month', type=int, required=True,
                        help='This field cannot be left blank')

    def post(self):
        ''' Add new apartment '''
        print(123456789)
        apartment_request_data = ApartmentView.parser.parse_args()

        name = apartment_request_data['name']
        number_of_rooms = apartment_request_data['number_of_rooms']
        location = apartment_request_data['location']
        rent_per_month = apartment_request_data['rent_per_month']

        new_appartment = Apartment(name, number_of_rooms, location, rent_per_month)
        new_appartment.save()

        return {
            "Message":"Apartment created successfully"
        }, 201