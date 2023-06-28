from django.db import models

# Create your models here.


class Item(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)


class Condition(models.Model):
    title = models.CharField(max_length=200)
    bmi = models.IntegerField()
    advice = models.TextField()

class BodyBuilderGoal(models.Model):
    item = models.TextField()

class DiabeticGoal(models.Model):
    item = models.TextField()

class ExpectantMotherGoal(models.Model):
    item = models.TextField()



