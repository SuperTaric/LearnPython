from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    # 这里处理模型
    return HttpResponse('Hello Django')