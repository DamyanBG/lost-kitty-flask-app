from marshmallow import fields, validate

from schemas.base_user_schema import BaseUserSchema
from utils.enums import RoleType


class UserRegisterSchema(BaseUserSchema):
    phone_number = fields.String(
        required=True, validate=validate.Length(min=6, max=255)
    )
    first_name = fields.String(required=True, validate=validate.Length(min=2, max=255))
    last_name = fields.String(required=True, validate=validate.Length(min=2, max=255))
    role = fields.Enum(RoleType)


class UserLoginSchema(BaseUserSchema):
    pass
