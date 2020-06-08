from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth.models import User, auth
from django.http import JsonResponse
# Create your views here.

def index(request):
    categories = Category.objects.all()
    posts = BlogPost.objects.order_by('-created_on')[:10]
    recent_post = posts[0]
    data = dict(categories=categories, posts=posts, recent_post=recent_post)
    return render(request,'nnanda/index.html',data)


def post(request, post_id):
    categories = Category.objects.all()
    post = BlogPost.objects.get(id=int(post_id))
    data = dict(categories=categories,post=post)
    return render(request, 'nnanda/post.html',data)


def login(request):
    if request.is_ajax():
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request,username=username, password=password)
        if user is not None:
            auth.login(request,user)
            return JsonResponse({'message':'success'})
        else:
            return JsonResponse({'message':'Invalid credentials'})
    else:
        return None
    

def register(request):
    if request.is_ajax():
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            return JsonResponse({"message":f"This username  ```{username}``` has been taken"})
        elif User.objects.filter(email=email).exists():
            return JsonResponse({"message":f"This email  ```{email}``` already exists"})
        else:
            user =  User.objects.create_user(username=username,email=email,password=password)
            user.save()
            return JsonResponse(dict(message="success"))
    


def logout(request):
    auth.logout(request)
    return JsonResponse({'message':'success'})