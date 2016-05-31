from django.db import models

from django.db import models
from django.core.urlresolvers import reverse
from settings import db


class AllrounderUser(models.Model):
    name = models.CharField(max_length=50)
    email_id = models.CharField(max_length=50, blank=False)
    age = models.IntegerField(blank=False)
    address = models.CharField(max_length=50, blank=False)
    is_service_provider = models.BooleanField(blank=False, default=False)
    image_path = models.CharField(max_length=100, default='s3_image_path', blank=True)
    lat = models.FloatField(blank=False)
    lon = models.FloatField(blank=False)
    gender = models.CharField(max_length=10)
    notifications = models.BooleanField(blank=False)
    services_used = models.CharField(max_length=20, blank=False)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    pincode = models.IntegerField(blank=False)
    
    class Meta:
        managed = True
        db_table = 'users'

    def save(self, *args, **kwargs):
        try:
            super(AllrounderUser, self).save(*args, **kwargs)
        except Exception as e:
            print "Exception occurred", e
            
    def delete(self, *args, **kwargs):
        super(AllrounderUser, self).delete(*args, **kwargs)


# Neo4j user models start here


# Create your models here.
class NodeHandle(models.Model):
    handle_id = models.CharField(max_length=64, unique=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def __unicode__(self):
        return 'NodeHandle for node %d' % self.node()['handle_id']

    def node(self):
        return db.get_node(self.handle_id, self.__class__.__name__)

    def delete(self, **kwargs):
        """
                Delete that node handle and the handles node.
                """
        db.delete_node(self.handle_id, self.__class__.__name__)
        super(NodeHandle, self).delete()
        return True

    delete.alters_data = True


class Movie(NodeHandle):

    def __unicode__(self):
        return self.title

    def _title(self):
        return self.node().get('title', 'Missing title')
    title = property(_title)

    def get_absolute_url(self):
        return reverse('movie-detail', args=[str(self.id)])

    def _actors(self):
        persons = []
        for person_id, roles in db.get_actors(self.handle_id):
            persons.append({'person': Person.objects.get(handle_id=person_id), 'roles': roles})
        return persons
    actors = property(_actors)

    def _directors(self):
        persons = []
        for person_id, in db.get_directors(self.handle_id):
            persons.append({'person': Person.objects.get(handle_id=person_id)})
        return persons
    directors = property(_directors)

    def _producers(self):
        persons = []
        for person_id, in db.get_producers(self.handle_id):
            persons.append({'person': Person.objects.get(handle_id=person_id)})
        return persons
    producers = property(_producers)

    def _writers(self):
        persons = []
        for person_id, in db.get_writers(self.handle_id):
            persons.append({'person': Person.objects.get(handle_id=person_id)})
        return persons
    writers = property(_writers)


class Person(NodeHandle):

    def __unicode__(self):
        return self.name

    def _name(self):
        return self.node().get('name', 'Missing name')
    name = property(_name)

    def get_absolute_url(self):
        return reverse('person-detail', args=[str(self.id)])