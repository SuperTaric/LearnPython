from django.shortcuts import render

# Create your views here.
from .models import Article

def index(request):
    blog_list = Article.objects.order_by('title')
    context = {'blog_list': blog_list}
    return render(request, 'blog.html', context)