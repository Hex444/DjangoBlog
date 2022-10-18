from django.contrib import admin
from django.urls import path, include

'''
the include func chops the already rendered part of the url in this
case http://localhost:8000/ is already rendered so that part is removed
and an empty string is sent to blog.urls file
'''
from django.contrib.auth import views as auth_views
from users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('register/',user_views.register,name='register'),
    path('login/',auth_views.LoginView.as_view(template_name='users/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='users/logout.html'),name='logout'),
]