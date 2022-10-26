from django.urls import path
from blog.models import Post
from . import views
from .views import (PostListView,
                    PostDetailView,
                    PostCreateView,
                    PostUpdateView,
                    PostDeleteView,
                    UserPostListView,

                    CommentCreateView,
)

urlpatterns = [
    # Post views
    path('',PostListView.as_view(),name='blog-home'),
    path('user/<str:username>',UserPostListView.as_view(),name='user-posts'),
    path('post/<int:pk>/',PostDetailView.as_view(),name='post-detail'),
    path('post/<int:pk>/update',PostUpdateView.as_view(),name='post-update'),
    path('post/<int:pk>/delete',PostDeleteView.as_view(),name='post-delete'),
    path('post/new/',PostCreateView.as_view(),name='post-create'),
    
    # Comment views
    path('comment/<str:slug>',CommentCreateView.as_view() ,name='comment-add'),
    
    
    # about page
    path('about/',views.about,name='blog-about'),
]

# autotemplate for class based views
# <app>/<model>_<viewtype>.html