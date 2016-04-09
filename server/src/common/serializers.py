from rest_framework import serializers

from .models import Users, ServicesMappedTo

class UserSerializers(serializers.ModelSerializer):
    users = serializers.Field('username', read_only=True)
    class Meta:
        model = Users
        fields = ('username ',)

class ServicesMappedToSerializers(serializers.ModelSerializer):
    services = serializers.HyperlinkedIdentityField('services')
    class Meta:
        model = ServicesMappedTo