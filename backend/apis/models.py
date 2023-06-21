from django.db import models


# Create your models here.
class OrderSum(models.Model):
    id = models.IntegerField(primary_key=True)
    orderNum = models.IntegerField()
    city = models.CharField(max_length=50)

    class Meta:
        db_table = 'orderSum'


class PositionInfo(models.Model):
    id = models.IntegerField(primary_key=True)
    post = models.CharField(max_length=20, null=True)
    level = models.CharField(max_length=20, null=True)

    class Meta:
        db_table = 'positionInfo'
