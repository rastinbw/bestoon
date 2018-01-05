from django.db import models

# Create your models here.
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