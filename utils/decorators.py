from flask import request
from werkzeug.exceptions import BadRequest, Forbidden

from managers.auth_manager import auth
from utils.enums import RoleType


def check_is_authorized(ownership_database_func, kwargs_key):
    def wrapper(func):
        def decorated_func(*args, **kwargs):
            print(args)
            print(kwargs)
            current_user = auth.current_user()
            is_owner = ownership_database_func(kwargs[kwargs_key], current_user.id)
            if not is_owner and not (current_user.role == RoleType.admin or current_user.role == RoleType.moderator):
                raise Forbidden("You do not have access to this resource.")
            return func(*args, **kwargs)
        return decorated_func
    return wrapper


def validate_schema(schema_name):
    def wrapper(func):
        def decorated_func(*args, **kwargs):
            data = request.get_json()
            schema = schema_name()
            errors = schema.validate(data)
            print(errors)
            if errors:
                raise BadRequest("You are not sending validate data.")
            return func(*args, **kwargs)

        return decorated_func

    return wrapper


def permission_required(permission):
    def wrapper(func):
        def decorated_func(*args, **kwargs):
            user = auth.current_user()
            if not user.role == permission:
                raise Forbidden("You do not have access to this resource")
            return func(*args, **kwargs)

        return decorated_func

    return wrapper
