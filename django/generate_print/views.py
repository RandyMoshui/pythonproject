import os

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from . import deal_data


def index(request):
    return render(request, "generate_print/index.html")


@csrf_exempt
def deal_order(request):
    myfile = request.FILES.get("order", None)

    if not myfile:
        context = {"info": "上传文件类型错误！"}
        return render(request, "generate_print/info.html", context, status=401)
    else:
        if myfile.content_type != "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet":
            context = {"info": "上传文件类型错误！"}
            return render(request, "generate_print/info.html", context, status=500)
        file_content = bytes()
        for chunk in myfile.chunks():
            file_content += chunk
        with open(myfile.name, 'wb+') as csv_file:
            csv_file.write(file_content)
        try:
            order_dict = deal_data.deal_data(myfile.name)
        except:
            context = {"info": "表格文件不匹配！请联系管理员！"}
            os.remove(myfile.name)
            return render(request, "generate_print/info.html", context, status=502)
        context = {
            'order_dict': order_dict,
            "length": len(order_dict),
            "index": [i for i in range(len(order_dict))],
            "filename": myfile.name
        }
        # print(context)
        return render(request, "generate_print/result.html", context=context)


def print_order(request, id=0, filename=""):
    order_dict = deal_data.deal_data(filename)
    order_dict = order_dict[id]
    goods = []
    for i in range(len(order_dict['商品名称'])):
        goods.append([order_dict['商品名称'][i], order_dict['商品属性'][i], order_dict["商品数量"][i]])
    context = {
        "order_dict": order_dict,
        "length": len(order_dict['商品名称']),
        "index": [i for i in range(len(order_dict['商品名称']))],
        # "name": order_dict['商品名称'],
        # "attr": order_dict['商品属性'],
        # "num": order_dict["商品数量"],
        "goods": goods,
    }
    return render(request, "generate_print/print.html", context=context)
