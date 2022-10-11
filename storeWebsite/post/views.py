from unicodedata import category
from django.shortcuts import render
from django.http import HttpResponse
from .models import Category, Post
# Create your views here.
def index(request):
    post = Post.objects.all()
    context = {'posts' : post}
    return render(request , 'post/index.html',context)  

def getPost(request,post_id):
    post = Post.objects.get(id = post_id)
    context = {'post':post}
    return render(request,'post/index.html',context)

def  getCategory(request):
    categorys = Category.objects.all()
    print("in Category")
    return render(request,'category/index.html',context={'categorys':categorys})

def findCategory(request,category_id):
    category = Category.objects.get(id = category_id)
    print(category.catDesc)
    return render(request , 'category/find.html',context={'category':category})