from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Token(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    token = models.CharField(max_length=128)

    def __str__(self):
        return "{}: token_{}".format(self.user,self.token)

class Expense(models.Model):
    description = models.CharField(max_length=256)
    date = models.DateTimeField()
    amount = models.BigIntegerField()
    user = models.ForeignKey('auth.User') #lazy many-to-one relationship

    def __str__(self):
        return "{}- {}".format(self.date,self.amount)

class Income(models.Model):
    description = models.CharField(max_length=256)
    date = models.DateTimeField()
    amount = models.BigIntegerField()
    user = models.ForeignKey('auth.User')

    def __str__(self):
        return "{}- {}".format(self.date,self.amount)