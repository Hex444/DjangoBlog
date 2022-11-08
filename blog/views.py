from django.shortcuts import render,get_object_or_404
from django.contrib.auth.models import User
from django.views.generic import ListView,DetailView,DeleteView,CreateView,UpdateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin

@login_required
def home(req):
    # context={
    #     'posts':smth.objects.all()
    # }
    return render(req,'blog/home.html',context={})


def about(req):
    return render(req,'blog/about.html',{'title':'About'})