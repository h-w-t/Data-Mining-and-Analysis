from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
# import csv

from .models import File, Iris, OrderSum, PositionInfo
from .serializers import FileSerializer, IrisSerializer
from .algorithms import Classifier


# ========= 文件上传 ========= #
class FileView(GenericAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer

    def post(self, request, *args, **kwargs):
        ser = self.serializer_class(data=request.data)
        if ser.is_valid(raise_exception=True):
            ser.save()
            return Response({
                "code": 201,
                "msg": "上传成功",
                "data": ser.data
            }, status=status.HTTP_201_CREATED)
        else:
            return Response({
                "code": 400,
                "msg": "上传失败",
                "data": ser.errors
            }, status=status.HTTP_400_BAD_REQUEST)
        # 存储到数据库

    '''读取文件到数据库'''
    # def read_file_to_database(self, request):
    #     file = request.file
    #     database_name = request.data.filename
    #     reader = csv.reader(file)
    #
    #     # 清空数据库
    #     database_name.objects.all().delete()
    #
    #     # 获取表头
    #     header = next(reader)
    #     num_cols = len(header)
    #     col_names = ["col_%d" % i for i in range(num_cols)]
    #     mapping = dict(zip(col_names, range(num_cols)))
    #
    #     for row in reader:
    #         # 从mapping里找出字段名称和索引
    #         field1 = mapping.get("col_0")
    #         field1_val = row[field1]
    #
    #         field2 = mapping.get("col_1")
    #         field2_val = row[field2]
    #
    #         # 更新或者创建对象
    #         obj, created = Iris.objects.create(
    #             **{col_names[field1]: field1_val},
    #             defaults={col_names[field2]: field2_val}
    #         )
    #
    #     print("成功读取文件至数据库"+database_name)
    ''''''


# ========= 鸢尾花数据集的查询 ========= #


# ========= 分类算法(决策树) ========= #
class IrisView(GenericAPIView):
    queryset = Iris.objects.all()
    serializer_class = IrisSerializer

    def get(self, request, *args, **kwargs):    # 鸢尾花数据集的查询
        queryset = self.get_queryset()  # 在get()方法中调用self.get_queryset()来获取queryset,而不是直接访问 self.queryset
        ser = self.serializer_class(queryset, many=True)
        return Response({
            "code": 200,
            "msg": "获取成功",
            "data": ser.data
        }, status=status.HTTP_200_OK)


"""
class ClassifyView(GenericAPIView):
    '''分类算法视图'''
    queryset = ClassifyResults.objects.all()
    serializer_class = ClassifyResultsSerializer
    def post(self, request, tree_height, child_node_num, *args, **kwargs):
        pass
"""

# ========= 分类算法(决策树) ========= #
