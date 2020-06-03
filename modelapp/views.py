from django.shortcuts import render
from .models import Blog, Article

# Create your views here.
def home(request):
    blog = Blog.objects
    article = Article.objects
    return render(request,'home.html',{'blog':blog, 'article':article})