from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from .models import OrderSum, PositionInfo, Iris, File


class FileSerializer(serializers.ModelSerializer):
    '''文件序列化器'''
    filename = serializers.CharField(max_length=50, required=False)
    timestamp = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', required=False)

    class Meta:
        model = File
        fields = "__all__"


class IrisSerializer(serializers.ModelSerializer):
    '''鸢尾花数据集序列化器'''

    class Meta:
        model = Iris
        exclude = ['id']
