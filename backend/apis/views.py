from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView

from .models import File
from .serializers import FileSerializer

# Create your views here.
class FileView(GenericAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer

    def post(self, request, *args, **kwargs):
        file_data = request.data
        ser = self.serializer_class(data=file_data)
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
