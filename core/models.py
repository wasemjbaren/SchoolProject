from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.




class User(AbstractUser):
    school_type = models.CharField(max_length=100)
    class_number = models.CharField(max_length=100)




class Classe(models.Model):
    class_type = models.CharField(max_length=100)

    def __str__(self):
        return self.class_type

class Class_number(models.Model):
    class_type = models.ForeignKey(Classe,on_delete=models.CASCADE)
    class_number = models.CharField(max_length=100,null=False)
    class_degree = models.IntegerField(null=False,default=10)
    class_description = models.TextField(max_length=250,null=False,default="description..")
    class_chairs = models.IntegerField(null=False,default=20)
    def __str__(self):
        return self.class_number