from marshmallow import fields
from marshmallow_sqlalchemy import ModelSchema

from server.model import Task
from server.schemas.file_schema import FileSchema
from server.schemas.web_schema import WebSchema


class TaskSchema(ModelSchema):
    files = fields.Nested(FileSchema, many=True)
    webs = fields.Nested(WebSchema, many=True)

    class Meta:
        model = Task