from django.contrib import admin
from django.urls import path, include

'''
the include func chops the already rendered part of the url in this
case http://localhost:8000/ is already rendered so that part is removed
and an empty string is sent to blog.urls file
'''

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
]