from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import reverse
from myblog.models import Post

# Create your views here.

# def index(request):
#     return HttpResponse("welcome to your first page")

def index(request):
    context = dict()
    context['blog_title'] = "Yogeshkannah Blog"
    # posts = [
    #     {'postname' : "post1",
    #      'postcontent' : "This is the first post",
    #      'id':1},

    #      {'postname' : "post2",
    #      'postcontent' : "This is the second post",
    #      'id':2},

    #      {'postname' : "post3",
    #      'postcontent' : "This is the third post",
    #      'id':3},

    #      {'postname' : "post4",
    #      'postcontent' : "This is the fourth post",
    #      'id':4},
    # ]
    posts = Post.objects.all()
    context['posts'] = posts
    return render(request,'myblog/index.html',context)

def detail(request,id):
    return render(request,"myblog/detail.html")


def blogs(request,id):
    return HttpResponse(f"Your current blog ID is {id}")

def old_url(request):
    return redirect(reverse("myblog:new_page_url"))

def new_view(request):
    return HttpResponse("This is new page..")