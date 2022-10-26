from urllib import request
from django.shortcuts import render,get_object_or_404
from .models import Post,Comment
from django.contrib.auth.models import User
from django.views.generic import ListView,DetailView,DeleteView,CreateView,UpdateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin

# @login_required
# def home(req):
#     context={
#         'posts':Post.objects.all()
#     }
#     return render(req,'blog/home.html',context=context)

class PostListView(LoginRequiredMixin,ListView):
    model=Post
    template_name='blog/home.html'
    context_object_name='posts'
    ordering=['-date_posted']
    # paginate_by=5

class UserPostListView(LoginRequiredMixin,ListView):
    model=Post
    template_name='blog/user_posts.html'
    context_object_name='posts'
    ordering=['-date_posted']
    paginate_by=5

    def get_queryset(self):
        user = get_object_or_404(User,username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

class PostDetailView(LoginRequiredMixin,DetailView):
    model=Post

class PostCreateView(LoginRequiredMixin,CreateView):
    model=Post
    fields=['title','content']

    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=Post
    fields=['title','content']

    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()    
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model=Post
    success_url='/'

    def test_func(self):
        post = self.get_object()    
        if self.request.user == post.author:
            return True
        return False


class CommentCreateView(LoginRequiredMixin,CreateView):
    model=Comment
    fields=['content']
    template_name="blog/comment_create.html"

def about(req):
    return render(req,'blog/about.html',{'title':'About'})