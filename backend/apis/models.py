from django.db import models


# ========= OrderSum ========= #
class OrderSum(models.Model):
    id = models.IntegerField(primary_key=True)
    orderNum = models.IntegerField()
    city = models.CharField(max_length=50)

    def __str__(self):
        return self.orderNum

    class Meta:
        db_table = 'ordersum'

# ========= PositionInfo ========= #
class PositionInfo(models.Model):
    id = models.IntegerField(primary_key=True)
    post = models.CharField(max_length=20, null=True)
    level = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.post
    
    class Meta:
        db_table = 'positioninfo'

# ========= Iris ========= #
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

# ========= Aprioridb ========= #
class Aprioridb(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    item1 = models.CharField(max_length=20, null=True)
    item2 = models.CharField(max_length=20, null=True)
    item3 = models.CharField(max_length=20, null=True)
    item4 = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.id

    class Meta:
        db_table = 'aprioridb'
        verbose_name = '关联规则'

# ========= ClassifyResults ========= #

# class ClassifyResults(models.Model):
#     tree_height = models.IntegerField()
#     child_node_num = models.IntegerField()
#     png = models.ImageField(upload_to='png/')
#
#     class Meta:
#         db_table = 'ClassifyResults'
#         verbose_name = '图片结果'

# ========= RegressionData ========= #
class RegressionData(models.Model):
    x = models.FloatField()
    y = models.FloatField()

    def __str__(self):
        return self.id

    class Meta:
        db_table = 'RegressionData'
        verbose_name = '回归数据'

# ========= BlobsDataSet ========= #
class BlobsDataSet(models.Model):
    x = models.FloatField()
    y = models.FloatField()
    label = models.IntegerField()

    def __str__(self):
        return self.id

    class Meta:
        db_table = 'BlobsDataSet'
        verbose_name = 'Blobs数据集'


# ========= MoonsDataSet ========= #
class MoonsDataSet(models.Model):
    x = models.FloatField()
    y = models.FloatField()
    label = models.IntegerField()

    def __str__(self):
        return self.id

    class Meta:
        db_table = 'MoonsDataSet'
        verbose_name = 'Moons数据集'