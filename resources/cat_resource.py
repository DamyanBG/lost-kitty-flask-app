from flask import request
from flask_restful import Resource

from utils.decorators import validate_schema, check_is_authorized
from managers.cat_manager import CatManager
from managers.auth_manager import auth
from schemas.request.cat_request_schema import CatRequestSchema
from schemas.response.cat_response_schema import CatResponseSchema


class CatResource(Resource):
    @auth.login_required
    @validate_schema(CatRequestSchema)
    def post(self):
        req_body = request.get_json()
        current_user = auth.current_user()
        print(current_user)
        req_body["owner_id"] = current_user.id
        cat = CatManager.add_cat(req_body)
        resp_schema = CatResponseSchema()
        return resp_schema.dump(cat)


class LostCatsResource(Resource):
    def get(self):
        cats = CatManager.select_lost_cats()
        resp_schema = CatResponseSchema()
        return resp_schema.dump(cats, many=True)


class FoundCatsResource(Resource):
    def get(self):
        cats = CatManager.select_found_cats()
        resp_schema = CatResponseSchema()
        return resp_schema.dump(cats, many=True)


class CatDetailsResource(Resource):
    def get(self, cat_id):
        cat = CatManager.select_cat_details(cat_id)
        resp_schema = CatResponseSchema()
        return resp_schema.dump(cat), 200
    

    @auth.login_required
    @check_is_authorized(CatManager.is_owner, "cat_id")
    def delete(self, cat_id):
        CatManager.delete_cat(cat_id)
        return {"message": "Succes"}, 204
