from django.db import models


# Create your models here.
class OrderSum(models.Model):
    id = models.IntegerField(primary_key=True)
    orderNum = models.IntegerField()
    city = models.CharField(max_length=50)

    def __str__(self):
        return self.orderNum

    class Meta:
        db_table = 'ordersum'


class PositionInfo(models.Model):
    id = models.IntegerField(primary_key=True)
    post = models.CharField(max_length=20, null=True)
    level = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.post
    
    class Meta:
        db_table = 'positioninfo'


class Iris(models.Model):
    id = models.IntegerField(primary_key=True)
    SpeL = models.FloatField()
    SpeW = models.FloatField()
    PetL = models.FloatField()
    PetW = models.FloatField()
    Species = models.CharField(max_length=20)

    def __str__(self):
        return self.Species

    class Meta:
        db_table = 'iris'
