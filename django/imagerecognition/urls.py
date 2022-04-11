from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index2"),  # 图片识别首页（上传）
    path('recognize', views.recognize, name="recognize"),  # 进行图片识别
]