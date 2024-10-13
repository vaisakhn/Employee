from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Employee(models.Model):
    user_object=models.OneToOneField(User,on_delete=models.CASCADE)
    department = models.CharField(max_length=200)
    role=models.CharField(max_length=200,null=True)
    created_date=models.DateField(auto_now=True)
    is_active=models.BooleanField(default=True)

    def __str__(self):
        return self.user_object