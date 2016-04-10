from rest_framework import serializers
# import models.Users
# from django.contrib.auth.models import  User, Group
from .models import Users


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('first_name', 'last_name', 'age', 'email_id')