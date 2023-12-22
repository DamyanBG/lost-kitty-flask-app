from flask import request
from flask_restful import Resource

from managers.auth_manager import AuthManager, auth
from managers.user_manager import UserManager
from schemas.request.user_request import UserRegisterSchema, UserLoginSchema
from schemas.response.user_response import UserResponseSchema
from utils.decorators import validate_schema
from utils.enums import RoleType


class RegisterUser(Resource):
    @validate_schema(UserRegisterSchema)
    def post(self):
        user_data = request.get_json()
        user_data["role"] = RoleType.user
        user = UserManager.register_user(request.get_json())
        token = AuthManager.encode_token(user)
        return {"token": token}, 201


class LoginUser(Resource):
    @validate_schema(UserLoginSchema)
    def post(self):
        request_body = request.get_json()
        user = UserManager.login_user(request_body)
        token = AuthManager.encode_token(user)
        return {"token": token, "id": user.id, "role": "user"}, 200
