from django.shortcuts import render,redirect
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("welcome to your first page")

def blogs(request,id):
    return HttpResponse(f"Your current blog ID is {id}")

def old_url(request):
    return redirect("new_url")

def new_view(request):
    return HttpResponse("This is new page..")