from flask_restful import Resource

from managers.cat_manager import CatManager
from managers.user_manager import UserManager
from schemas.response.cat_response_schema import CatResponseWithContactInfo


class MicrochipSearch(Resource):
    def get(self, microchip):
        cat = CatManager.select_by_microchip(microchip)
        
        if not cat:
            return {
                "message": f"The cat with microchip {microchip} is not existing in our database."
            }, 200
        
        contact_person = UserManager.select_by_id(cat.owner_id)
        cat.contact_info = {
        "person": f"{contact_person.first_name} {contact_person.last_name}",
        "email": contact_person.email,
        "phone_number": contact_person.phone_number,
    }
        resp_schema = CatResponseWithContactInfo()
        return resp_schema.dump(cat), 200


class PassportIdSearch(Resource):
    def get(self, passport_id):
        cat = CatManager.select_by_passport_id(passport_id)
        if not cat:
            return {
                "message": f"The cat with passport id {passport_id} is not existing in our database."
            }, 200
        
        contact_person = UserManager.select_by_id(cat.owner_id)
        cat.contact_info = {
        "person": f"{contact_person.first_name} {contact_person.last_name}",
        "email": contact_person.email,
        "phone_number": contact_person.phone_number,
    }
        resp_schema = CatResponseWithContactInfo()
        return resp_schema.dump(cat), 200
