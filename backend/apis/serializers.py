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

# class ClassifyResultsSerializer(serializers.ModelSerializer):
#     '''分类结果序列化器'''
#
#     class Meta:
#         model = ClassifyResults
#         fields = "__all__"

# ========= RegressionData序列化器 ========= #
class RegressionDataSerializer(serializers.ModelSerializer):
    '''回归数据序列化器'''

    class Meta:
        model = OrderSum
        fields = "__all__"

# ========= 关联规则结果序列化器 ========= #
class AprioriResultSerializer(serializers.Serializer):
    data = serializers.ListField()
