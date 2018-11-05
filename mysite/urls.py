from django.urls import path, include, re_path
from django.contrib import admin
from django.contrib.auth import views
from django.contrib.auth.views import LogoutView
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^accounts/login/$', views.login, name='login'),
    re_path(r'^accounts/logout/$', views.logout, name='logout', kwargs={'next_page': '/'}),
    re_path(r'^accounts/login/$', views.LoginView.as_view(), name='login'),
    re_path(r'^accounts/logout/$', views.LogoutView.as_view(), name='logout', kwargs={'next_page': '/'}),
    path('', include('blog.urls')),
]
