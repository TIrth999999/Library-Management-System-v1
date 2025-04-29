from django.db import models
from django.contrib.auth.models import User

class Penalty(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.IntegerField(max_length = 10000,default = 0)

    def __str__(self):
        return self.user
    
class Borrowed(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length = 122,default = "NULL")
    quantity = models.IntegerField(max_length=10,default=0)
    approved = models.BooleanField(default=False)
    date = models.DateField()

    def __str__(self):
        return self.name