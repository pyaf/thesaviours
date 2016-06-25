from django.db import models

class Patients(models.Model):
    
    firstname = models.CharField(max_length = 100)
    lastname = models.CharField(max_length = 100)
    location = models.TextField(max_length = 100)
    level = models.IntegerField()
    age = models.IntegerField()
    gender = models.TextField()
    comment = models.TextField()
    
    def __str__(self):
        return  '%s %s' % (self.firstname, self.location)
