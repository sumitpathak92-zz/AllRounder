from django.db import models
import datetime
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator

class Users(models.Model):
    def __init__(self, username, email_id, created = None):
        self.email_id = email_id
        self.username = username
        self.created or datetime.now()

    username = models.CharField(max_length=20)
    email_id = models.CharField(max_length=100)
    join_date = models.DateTimeField(auto_now=True)

class ServicesMappedTo(models.Model):
    services = models.ForeignKey(Users)

