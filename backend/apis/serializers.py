from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from .models import OrderSum, PositionInfo, Iris, File


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
        exclude = ['id']

# ========= 购物清单序列化器 ========= #

# class ClassifyResultsSerializer(serializers.ModelSerializer):
#     '''分类结果序列化器'''
#
#     class Meta:
#         model = ClassifyResults
#         fields = "__all__"
