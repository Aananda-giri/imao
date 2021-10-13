from django.db import models

class Person(models.Model):
    hot_votes = models.IntegerField()
    not_votes = models.IntegerField()

#class 

