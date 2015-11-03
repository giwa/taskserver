from marshmallow import fields
from marshmallow_sqlalchemy import ModelSchema

from server.model import Web
from server.schemas.task_schema import TaskSchema


class WebSchema(ModelSchema):
    task = fields.Nested(TaskSchema, many=False)

    class Meta:
        model = Web