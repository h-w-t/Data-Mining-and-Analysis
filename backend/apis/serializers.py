from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from .models import OrderSum, PositionInfo, Iris, File, Aprioridb, RegressionData


# ========= 文件序列化器 ========= #
class FileSerializer(serializers.ModelSerializer):
    filename = serializers.CharField(max_length=50, required=False)
    timestamp = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', required=False)

    class Meta:
        model = File
        fields = "__all__"


# ========= 鸢尾花数据集序列化器 ========= #
class IrisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Iris
        fields = "__all__"

# ========= 购物清单序列化器 ========= #
class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Aprioridb
        fields = "__all__"

# ========= RegressionData序列化器 ========= #
class RegressionDataSerializer(serializers.ModelSerializer):
    '''回归数据序列化器'''

    class Meta:
        model = RegressionData
        fields = "__all__"

# ========= 关联规则参数序列化器 ========= #
class AprioriParameterSerializer(serializers.Serializer):
    min_sup = serializers.FloatField()
    min_conf = serializers.FloatField()

# ========= List序列化器 ========= #
class ListSerializer(serializers.Serializer):
    data = serializers.ListField()

# ========= 聚类数据集序列化器 ========= #
class ClusterDataSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    x = serializers.FloatField()
    y = serializers.FloatField()
    # label = serializers.IntegerField()

class DBSCANResultSerializer(serializers.Serializer):
    # id = serializers.IntegerField()
    x = serializers.FloatField()
    y = serializers.FloatField()
    predict_result = serializers.IntegerField()

# ========= 聚类参数集序列化器 ========= #
class KmeansParameterSerializer(serializers.Serializer):
    k = serializers.IntegerField()

class DBSCANParameterSerializer(serializers.Serializer):
    eps = serializers.FloatField()
    min_samples = serializers.IntegerField()

# ========= 聚类结果序列化器 ========= #

# ========= 分类参数序列化器 ========= #
class ClassifyParameterSerializer(serializers.Serializer):
    tree_height = serializers.IntegerField()
    child_node_num = serializers.IntegerField()
