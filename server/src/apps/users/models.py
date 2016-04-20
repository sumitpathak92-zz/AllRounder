from django.db import models

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