from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from models import AllrounderUser

class AllrounderUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AllrounderUser
        fields_value = ('id', 'name', 'email_id', 'age', 'address', 'is_service_provider', 'image_path', 'lat', 'lon', 'gender', 'notifications', 'services_used', 'city', 'state', 'pincode')
        validators = [
            UniqueTogetherValidator(
                queryset=AllrounderUser.objects.all(),
                fields=('id', 'email_id'),
                message="User Already Exists"
            )
        ]

