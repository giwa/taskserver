from marshmallow import fields
from marshmallow_sqlalchemy import ModelSchema

from server.model import User, Visit, Web, File, Task


class TaskSchema(ModelSchema):
    class Meta:
        model = Task


class UserSchema(ModelSchema):
    class Meta:
        model = User


class VisitSchema(ModelSchema):
    class Meta:
        model = Visit


class WebSchema(ModelSchema):
    class Meta:
        model = Web


class FileSchema(ModelSchema):

    class Meta:
        model = File


# File schema
FileSchema._declared_fields['web'] = fields.Nested(WebSchema, many=False, exclude=('files', 'task', ))
FileSchema._declared_fields['task'] = fields.Nested(TaskSchema, many=False, exclude=('files', 'webs', ))


# Task schema
TaskSchema._declared_fields['webs'] = fields.Nested(WebSchema, many=True, exclude=('task', 'files'))
TaskSchema._declared_fields['files'] = fields.Nested(FileSchema, many=True, exclude=('task', 'web'))

# User schema
UserSchema._declared_fields['visits'] = fields.Nested(VisitSchema, many=True, exclude=('user', ))

# Visit schema
VisitSchema._declared_fields['user'] = fields.Nested(UserSchema, many=False, exclude=('visit', ))
VisitSchema._declared_fields['web'] = fields.Nested(WebSchema, many=False, exclude=('visit', 'files',))

# WebSchema
WebSchema._declared_fields['files'] = fields.Nested(FileSchema, many=True, exclude=('webs', ))
WebSchema._declared_fields['task'] = fields.Nested(TaskSchema, many=False, exclude=('webs', ))
