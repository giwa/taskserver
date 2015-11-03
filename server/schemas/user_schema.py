from marshmallow import fields
from marshmallow_sqlalchemy import ModelSchema

from server.model import User
from server.schemas.visit_schema import VisitSchema


class UserSchema(ModelSchema):
    visits = fields.Nested(VisitSchema, many=True)

    class Meta:
        model = User