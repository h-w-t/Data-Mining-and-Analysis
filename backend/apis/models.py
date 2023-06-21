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

class File(models.Model):
    file = models.FileField(upload_to='files/')
    filename = models.CharField(max_length=50, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.filename

    class Meta:
        db_table = 'file'
        verbose_name = '文件'
