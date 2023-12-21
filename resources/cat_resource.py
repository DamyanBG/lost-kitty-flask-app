from flask import request
from flask_restful import Resource

from utils.decorators import validate_schema
from managers.cat_manager import CatManager
from managers.auth_manager import auth
from schemas.request.cat_request_schema import CatRequestSchema
from schemas.response.cat_response_schema import CatResponseSchema


class CatResource(Resource):
    @auth.login_required
    @validate_schema(CatRequestSchema)
    def post(self):
        req_body = request.get_json()
        cat = CatManager.add_cat(req_body)
        resp_schema = CatResponseSchema()
        return resp_schema.dump(cat)


class CatsResource(Resource):
    def get(self):
        cats = CatManager.select_all_cats()
        resp_schema = CatResponseSchema()
        return resp_schema.dump(cats, many=True)
