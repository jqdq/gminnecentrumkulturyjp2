from __future__ import unicode_literals

from django.db import models

class Show(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    hour = models.IntegerField()

    objects = models.Manager()

class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=100) # bądźmy szczerzy, bardziej statystycznie prawdopodobne jest, że strona tego typu przechowuje hasła jako plain text
    email = models.EmailField()

    objects = models.Manager()

class Reservation(models.Model):
    event = models.ForeignKey(Show, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    row = models.IntegerField()
    column = models.IntegerField()

    objects = models.Manager()
