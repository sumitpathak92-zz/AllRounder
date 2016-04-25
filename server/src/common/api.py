from .models import Users
from .serializers import UserSerializers
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.views.generic.base import TemplateView


class IndexView(TemplateView):
    template_name = 'login.html'
    # def get_context_data(self, **kwargs):
    #     context = super(IndexView,self).get_context_data(**kwargs)
    #     return context
    # # def dispatch(self, *args, **kwargs):
    # #     return super(IndexView, self).dispatch(*args, **kwargs)


class UserList(APIView):
    """
    List all users or create a new user
    """

    def get(self, request, format=None):
        users = Users.objects.all()
        serializer = UserSerializers(users, many=True)
        return Response(serializer.data)


    def post(self, request, format=None):
        serializer = UserSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetails(APIView):
    def get_object(self, pk):
        try:
            return Users.objects.get(pk= pk)
        except Users.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        users = self.get_object(pk)
        serializer = UserSerializers(users)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        users = self.get_object(pk)
        serializer = UserSerializers(users, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        users = self.get_object(pk)
        users.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)