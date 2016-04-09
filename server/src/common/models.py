from django.db import models
from pygments.lexers import get_all_lexers
from datetime import datetime
# from serializers import UserSerializers
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator

class Users(models.Model):
    created_at_time = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=20, blank=False)
    last_name = models.CharField(max_length=20, blank=False)
    age = models.IntegerField(blank=False)
    email_id = models.CharField(max_length=50, blank=False)

    class Meta:
        ordering = ('created_at_time',)

