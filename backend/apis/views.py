from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .algorithms import Apriori, Clustering, Regression
from .models import File, Iris, Aprioridb, RegressionData, BlobsDataSet, MoonsDataSet
from .serializers import FileSerializer, IrisSerializer, OrderSerializer, RegressionDataSerializer, \
    ListSerializer, ClusterDataSerializer, AprioriParameterSerializer, KmeansParameterSerializer, \
    ClassifyParameterSerializer, DBSCANParameterSerializer


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


# ========= 关联规则算法 ========= #
# 购物清单的查询
class OrderView(GenericAPIView):
    queryset = Aprioridb.objects.all()
    serializer_class = OrderSerializer

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        ser = self.serializer_class(queryset, many=True)
        return Response({
            "code": 200,
            "msg": "获取成功",
            "data": ser.data
        }, status=status.HTTP_200_OK)


class AprioriView(APIView):
    min_sup = None
    min_conf = None

    def post(self, request, min_sup, min_conf, *args, **kwargs):  # 参数的获取
        self.min_sup = min_sup
        self.min_conf = min_conf
        ser = AprioriParameterSerializer(data={
            "min_sup": self.min_sup,
            "min_conf": self.min_conf
        })
        if ser.is_valid(raise_exception=True):
            return Response({
                "code": 200,
                "msg": "参数获取成功",
                "data": ser.data
            }, status=status.HTTP_200_OK)
        else:
            return Response({
                "code": 400,
                "msg": "参数获取失败",
                "data": ser.errors
            }, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        apriori = Apriori(self.min_sup, self.min_conf)
        result = apriori.result()
        ser = ListSerializer(instance={
            "data": result
        })
        return Response({
            "code": 200,
            "msg": "获取置信度矩阵成功",
            "data": ser.data['data']
        }, status=status.HTTP_200_OK)


# ========= 聚类算法(决策树) ========= #
# 初始数据集的获取
class BlobsDataView(GenericAPIView):
    queryset = BlobsDataSet.objects.all()
    serializer_class = ClusterDataSerializer

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        ser = self.serializer_class(instance=queryset, many=True)
        return Response({
            "code": 200,
            "msg": "获取成功",
            "data": ser.data
        }, status=status.HTTP_200_OK)


class MoonsDataView(GenericAPIView):
    queryset = MoonsDataSet.objects.all()
    serializer_class = ClusterDataSerializer

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        ser = self.serializer_class(queryset, many=True)
        return Response({
            "code": 200,
            "msg": "获取成功",
            "data": ser.data
        }, status=status.HTTP_200_OK)


# 初始数据集的获取(Echarts)
class BlobsDataForEchartsView(APIView):
    def get(self, request, *args, **kwargs):
        cluster = Clustering()
        scatters_loc = cluster.original_blobs_data_for_echarts()
        ser = ListSerializer(instance={
            "data": scatters_loc
        })
        return Response({
            "code": 200,
            "msg": "获取成功",
            "data": ser.data['data']
        }, status=status.HTTP_200_OK)

class MoonsDataForEchartsView(APIView):
    def get(self, request, *args, **kwargs):
        cluster = Clustering()
        scatters_loc = cluster.original_moons_data_for_echarts()
        ser = ListSerializer(instance={
            "data": scatters_loc
        })
        return Response({
            "code": 200,
            "msg": "获取成功",
            "data": ser.data['data']
        }, status=status.HTTP_200_OK)


class KmeansView(APIView):
    # 参数的获取
    def __init__(self):
        self.k = None

    def post(self, request, k, *args, **kwargs):
        self.k = k
        ser = KmeansParameterSerializer(data={
            'k': k})
        if ser.is_valid(raise_exception=True):
            return Response({
                "code": 200,
                "msg": "参数获取成功",
                "data": ser.data
            }, status=status.HTTP_200_OK)
        else:
            return Response({
                "code": 400,
                "msg": "参数获取失败",
                "data": ser.errors
            }, status=status.HTTP_400_BAD_REQUEST)

class DBSCANView(APIView):
    def __init__(self):
        self.eps = None
        self.min_samples = None

    # 参数的获取
    def post(self, request, eps, min_samples, *args, **kwargs):
        self.eps = float(eps)
        self.min_samples = int(min_samples)
        ser = DBSCANParameterSerializer(data={
            "eps": self.eps,
            "min_samples": self.min_samples
        })
        if ser.is_valid(raise_exception=True):
            return Response({
                "code": 200,
                "msg": "参数获取成功",
                "data": ser.data
            }, status=status.HTTP_200_OK)
        else:
            return Response({
                "code": 400,
                "msg": "参数获取失败",
                "data": ser.errors
            }, status=status.HTTP_400_BAD_REQUEST)


# ========= 分类算法(决策树) ========= #
# 鸢尾花数据集的查询
class IrisView(GenericAPIView):
    queryset = Iris.objects.all()
    serializer_class = IrisSerializer

    def get(self, request, *args, **kwargs):  # 鸢尾花数据集的查询
        queryset = self.get_queryset()  # 在get()方法中调用self.get_queryset()来获取queryset,而不是直接访问 self.queryset
        ser = self.serializer_class(queryset, many=True)
        return Response({
            "code": 200,
            "msg": "获取成功",
            "data": ser.data
        }, status=status.HTTP_200_OK)


class ClassifyView(APIView):
    def __init__(self):
        self.tree_height = None
        self.child_node_num = None

    # 参数的获取
    def post(self, request, tree_height, child_node_num, *args, **kwargs):
        self.tree_height = tree_height
        self.child_node_num = child_node_num
        ser = ClassifyParameterSerializer(data={
            'tree_height': tree_height,
            'child_node_num': child_node_num})
        if ser.is_valid(raise_exception=True):
            return Response({
                "code": 200,
                "msg": "参数获取成功",
                "data": ser.data
            }, status=status.HTTP_200_OK)
        else:
            return Response({
                "code": 400,
                "msg": "参数获取失败",
                "data": ser.errors
            }, status=status.HTTP_400_BAD_REQUEST)


# ========= 回归算法 ========= #
# 初始数据集的查询
class RegressionDataView(GenericAPIView):
    queryset = RegressionData.objects.all()
    serializer_class = RegressionDataSerializer

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        ser = self.serializer_class(queryset, many=True)
        return Response({
            "code": 200,
            "msg": "获取成功",
            "data": ser.data
        }, status=status.HTTP_200_OK)

class RegressionDataForEchartsView(APIView):
    def get(self, request, *args, **kwargs):
        regression = Regression()
        scatters_loc = regression.original_regression_data_for_echarts()
        ser = ListSerializer(instance={
            "data": scatters_loc
        })
        return Response({
            "code": 200,
            "msg": "获取成功",
            "data": ser.data['data']
        }, status=status.HTTP_200_OK)
