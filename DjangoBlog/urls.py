from django.contrib import admin
from django.urls import path, include

'''
the include func chops the already rendered part of the url in this
case http://localhost:8000/ is already rendered so that part is removed
and an empty string is sent to blog.urls file
'''
from django.contrib.auth import views as auth_views
from users import views as user_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('register/',user_views.register,name='register'),
    path('login/',auth_views.LoginView.as_view(template_name='users/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='users/logout.html'),name='logout'),
    path('profile/',user_views.profile,name='profile'),

    path('password-reset/',
    auth_views.PasswordResetView.as_view(template_name='users/password_reset.html')
    ,name='password_reset'),

    path('password-reset-complete',
    auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html')
    ,name='password_reset_complete'),

    path('password-reset/done/',
    auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html')
    ,name='password_reset_done'),

    path('password-reset-confirm/<uidb64>/<token>/',
    auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html')
    ,name='password_reset_confirm'),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)