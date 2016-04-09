from rest_framework import generics, permissions

from .serializers import UserSerializers, ServicesMappedToSerializers
from .models import Users, ServicesMappedTo

class UsersList(generics.ListCreateAPIView):
    queryset = Users.objects.all()
    model = Users
    serializer_class = UserSerializers
    permission_classes = [
        permissions.AllowAny
    ]

    # def get_queryset(self):
    #     queryset = super(UsersList, self).get_queryset()
    #     return queryset.filter(users__username=self.kwargs.get('username'))

class ServicesList(generics.ListCreateAPIView):

    model = ServicesMappedTo
    serializer_class = ServicesMappedToSerializers
    permission_classes = [
        permissions.AllowAny
    ]