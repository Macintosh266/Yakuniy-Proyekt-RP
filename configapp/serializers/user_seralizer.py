from rest_framework import serializers
from configapp.models.auth_user import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["phone", "email", "password", "is_admin",  "is_teacher","is_student"]
        read_only_fields = ["is_active"]