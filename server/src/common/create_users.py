from models import Users
from serializers import UserSerializers

from  rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

user = Users(first_name='Sumit', last_name='Pathak', age='24', email_id='pathaksumit92@gmail.com')
user.save()

serializer = UserSerializers(user)
serializer.data

content = JSONRenderer().render(serializer.data)
content


from django.utils.six import BytesIO

stream = BytesIO(content)
data = JSONParser().parse(stream)

serializer = UserSerializers(data = data)
serializer.is_valid()

serializer.validated_data()

serializer.save()

serializer = UserSerializers(Users.objects.all(), many=True)
serializer.data
