from marshmallow import fields

from schemas.base_cat_schema import BaseCatSchema


class CatResponseSchema(BaseCatSchema):
    id = fields.Integer(required=True)
    photos_urls = fields.List(fields.String(), required=True)
    owner_id = fields.Integer()


class CatResponseWithContactInfo(CatResponseSchema):
    contact_info = fields.Dict(keys=fields.String(), values=fields.String())
