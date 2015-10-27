from marshmallow_sqlalchemy import ModelSchema

from server.model import User, Visit, Web, File, Task

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

class TaskSchema(ModelSchema):
    class Meta:
        model = Task
