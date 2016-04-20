from models import AllrounderUser
from serializers import AllrounderUserSerializer

from rest_framework.views import APIView
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status

class AllrounderUserAPI(APIView):
    """
    Gives JSON response of all the registered application users
    """

    def get(self, request, format=None):
        users = AllrounderUser.objects.all()
        user_serializer = AllrounderUserSerializer(users, many=True)
        return Response(user_serializer.data)

class AllrounderUserDetailAPI(APIView):
    """
    Gives user details of registered user given its user_id
    """

    def get_user_details(self, id):
        try:
            return AllrounderUser.objects.get(id=id)
        except AllrounderUser.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        user = self.get_user_details(id)
        user_serializer = AllrounderUserSerializer(user)
        return Response(user_serializer.data)