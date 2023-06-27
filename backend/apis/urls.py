"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from .views import FileView, IrisView, OrderView, AprioriView, BlobsDataView, MoonsDataView, KmeansView, \
    RegressionDataView, ClassifyView, BlobsDataForEchartsView, MoonsDataForEchartsView, RegressionDataForEchartsView, \
    DBSCANView

urlpatterns = [
    path('file/upload/', FileView.as_view(), name='file-upload'),

    path('rules/all/', OrderView.as_view(), name='rules-all'),
    path('rules/parameter/<min_sup>&<min_conf>/', AprioriView.as_view(), name='rules-parameter'),

    path('cluster/data/blobs/', BlobsDataView.as_view(), name='cluster-blobs-data'),
    path('cluster/data/blobs/echarts/', BlobsDataForEchartsView.as_view(), name='cluster-blobs-data-for-echarts'),
    path('cluster/data/moons/', MoonsDataView.as_view(), name='cluster-moons-data'),
    path('cluster/data/moons/echarts/', MoonsDataForEchartsView.as_view(), name='cluster-moons-data-for-echarts'),
    # path('cluster/kmeans/parameter/<int:k>/', KmeansView.as_view(), name='cluster-kmeans-parameter'),
    path('cluster/dbscan/parameter/<eps>&<min_samples>/', DBSCANView.as_view(), name='cluster-DBSCAN-parameter'),

    path('regression/all/', RegressionDataView.as_view(), name='regression-all'),
    path('regression/data/echarts/', RegressionDataForEchartsView.as_view(), name='regression-data-for-echarts'),

    path('classify/all/', IrisView.as_view(), name='iris-all'),
    path('classify/<int:tree_height>&<int:child_node_num>/', ClassifyView.as_view(), name='classify-parameter'),
    path('classify/result/', ClassifyView.as_view(), name='classify-result'),
]
