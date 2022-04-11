from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from . import baiduocr
import time


# Create your views here.

# 图片识别首页
def index(request):
    return render(request, "imagerecognition/index.html")


@csrf_exempt
def recognize(request):
    myfile = request.FILES.get("pic", None)

    if not myfile:  # 当数据没有值时
        context = {"info": "没有选择上传文件！"}
        return render(request, "imagerecognition/info.html", status=404, context=context)
    else:
        file_name = myfile.name
        file_type = request.FILES.get("pic", None).content_type
        all_type_list = ['image/jpeg', 'image/png']
        all_name_list = ['jpg', 'jpeg', 'png']
        # print(file_type)
        # print(myfile)
        # print(file_name)
        file_content = bytes()
        # 生产上传后的文件名
        # file_name = str(time.time()) + "." + file_name.split('.').pop()
        # print(file_name)
        file_name = file_name.split('.')
        # print(file_name)
        if file_type in all_type_list and len(file_name) <= 2 and file_name[1] in all_name_list:
            for chunk in myfile.chunks():
                file_content = file_content + chunk
            context = {"result": baiduocr.main(file_content)}
            return render(request, "imagerecognition/result.html", context)
        else:
            context = {"info": "这种文件类型不被允许！"}
            return render(request, "imagerecognition/info.html", status=400, context=context)