from django.db import models
# from neo4j.db import models

class Users(models.Model):
    created_at_time = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=20, blank=False)
    last_name = models.CharField(max_length=20, blank=False)
    age = models.IntegerField(blank=False)
    email_id = models.CharField(max_length=50, blank=False)

    class Meta:
        ordering = ('created_at_time',)


# # neo4j model for a person
# class Person(models.NodeModel):
#     name = models.StringProperty()
#     age = models.IntegerProperty()
#
#     friends = models.Relationship('self', rel_type='friends_with')
