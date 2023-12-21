from marshmallow import fields

from schemas.base_cat_schema import BaseCatSchema


class CatRequestSchema(BaseCatSchema):
    photos = fields.List(fields.String(), required=True)
