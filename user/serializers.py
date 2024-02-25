from rest_framework import serializers
from collections import OrderedDict
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class UserPatchSingle(UserSerializer):
    def get_fields(self):
        new_fields = OrderedDict()

        for name, field in super().get_fields().items():
            if name != 'id':
                field.required = False
                new_fields[name] = field
            else:
                new_fields[name] = field
        return dict(new_fields)

class UserPatch(UserPatchSingle):
    id = serializers.IntegerField()

