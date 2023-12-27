from flask_restful import Resource

from managers.auth_manager import AuthManager, auth
from managers.user_manager import UserManager
from schemas.response.user_response import UserResponseSchema, UserInfoResponseSchema


class UserResource(Resource):
    @auth.login_required
    def get(self):
        current_user = auth.current_user()
        del current_user.password
        user_schema = UserInfoResponseSchema()
        return user_schema.dump(current_user)
