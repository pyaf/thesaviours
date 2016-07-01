from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
class Patients(models.Model):
    
    firstname = models.CharField(max_length = 20)
    lastname = models.CharField(max_length = 20)
    location = models.CharField(max_length = 200)
    level = models.IntegerField(validators=[MinValueValidator(1),
                                       MaxValueValidator(3)])
    age = models.IntegerField()
    gender = models.CharField(max_length=6)
    comment = models.CharField(max_length = 200)
    
    def __str__(self):
        return  'name : %s %s | location : %s | level : %d | Age : %d | Gender : %s | Comment : %s' % (self.firstname,self.lastname, self.location,
        	self.level, self.age, self.gender,self.comment)
