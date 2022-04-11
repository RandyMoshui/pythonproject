from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
# Create your views here.


def index(request):
    context = {
        "function": {"图片识别": reverse('index2'), "打印订单": reverse('index3')},
    }
    return render(request, 'index.html', context=context)


