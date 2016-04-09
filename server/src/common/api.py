from rest_framework import generics, permissions, viewsets
from django.contrib.auth.models import User, Group
from .serializers import UserSerializers
# from .models import Users, ServicesMappedTo
from .models import Users
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http import HttpResponse
from .serializers import UserSerializers

class JSONResponse(HttpResponse):
    """
    An HTTPResponse that renders its contents into JSON
    """

    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@csrf_exempt
def user_list(request):
    """

    """
    if request.method=='GET':
        users = Users.objects.all()
        serializer = UserSerializers(users, many=True)
        return JSONResponse(serializer.data)

    elif request.method=='POST':
        data = JSONParser().parse(request)
        serializer = UserSerializers(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)


@csrf_exempt
def user_detail(request):
    try:
        users = Users.objects.get()
    except Users.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = UserSerializers(users)
        return JSONResponse(serializer.data)

    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = UserSerializers(users, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=404)

    elif request.method == 'DELETE':
        users.delete()
        return HttpResponse(status=204)