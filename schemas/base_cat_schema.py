from marshmallow import Schema, fields, validate

from utils.enums import CatStatus


class BaseCatSchema(Schema):
    cat_name = fields.String(required=True, validate=validate.Length(min=2, max=255))
    microchip = fields.String(validate=validate.Length(min=2, max=255))
    passport_id = fields.String(validate=validate.Length(min=2, max=255))
    owner_id = fields.Integer(required=True)
    status = fields.Enum(CatStatus, required=True)
