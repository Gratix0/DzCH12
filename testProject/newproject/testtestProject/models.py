from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)


class Mechanism(models.Model):
    switch = models.CharField(max_length=200)
    keycup = models.CharField(max_length=200)

class Preferences(models.Model):
    switchP = models.CharField(max_length=200)
    keycupP = models.CharField(max_length=200)
    color = models.CharField(max_length=200)

class AllRange(models.Model):
    keyboard = models.BigIntegerField()
    switch = models.BigIntegerField()
    keycup = models.BigIntegerField()
    
class Spot(models.Model):
    adress = models.CharField(max_length=300)
    localRangeAllProduct = models.BigIntegerField()
    registry = models.DateField()
