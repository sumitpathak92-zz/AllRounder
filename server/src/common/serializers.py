from rest_framework import serializers
# import models.Users
# from django.contrib.auth.models import  User, Group
from .models import Users


class UserSerializers(serializers.HyperlinkedModelSerializer):
    first_name = serializers.CharField(required=True, allow_blank=False, max_length=20)
    last_name = serializers.CharField(required=True, allow_blank=False, max_length=20)
    age = serializers.IntegerField(required=True, allow_null=False)
    email_id = serializers.CharField(required=True, allow_blank=False)

    def create(self, validated_data):
        """
        Create and Return a new USER instance
        """
        return Users.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing User instance, given validated data
        """
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.age = validated_data.get('age', instance.age)
        instance.email_id = validated_data.get('email_id', instance.email_id)
        instance.save()
        return instance

# class GroupSerializers(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Group
#         fields = ('url', 'name')



# serializer = UserSerializers(user)

# class ServicesMappedToSerializers(serializers.ModelSerializer):
#     services = serializers.HyperlinkedIdentityField('services')
#     class Meta:
#         model = ServicesMappedTo