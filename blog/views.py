from django.shortcuts import render
from django.http import HttpResponse
from .models import Post




def home(req):
    context={
        'posts':Post.objects.all()
    }
    return render(req,'blog/home.html',context=context)

def about(req):
    return render(req,'blog/about.html',{'title':'About'})