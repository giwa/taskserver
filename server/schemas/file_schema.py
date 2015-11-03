from marshmallow import fields
from marshmallow_sqlalchemy import ModelSchema

from server.model import File
from server.schemas.web_schema import WebSchema
from server.schemas.task_schema import TaskSchema


class FileSchema(ModelSchema):
    web = fields.Nested(WebSchema, many=False)
    task = fields.Nested(TaskSchema, many=False)

    class Meta:
        model = File