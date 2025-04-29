from django.db import models
from django.contrib.auth.models import User

class Books(models.Model):
    name = models.CharField(max_length = 122,default = "NULL")
    subject = models.CharField(max_length = 122,default = "NULL")
    author = models.CharField(max_length = 10,default = "NULL")
    quantity = models.IntegerField(max_length=100,default=1)
    isBorrowed = models.BooleanField(default=False)

    def __str__(self):
        return self.name