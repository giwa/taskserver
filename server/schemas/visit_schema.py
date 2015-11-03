from marshmallow import fields
from marshmallow_sqlalchemy import ModelSchema

from server.model import Visit
from server.schemas.user_schema import UserSchema
from server.schemas.web_schema import WebSchema

class VisitSchema(ModelSchema):
    user = fields.Nested(UserSchema, many=False)
    web = fields.Nested(WebSchema, many=False)

    class Meta:
        model = Visit