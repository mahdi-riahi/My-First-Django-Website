from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.blog_home_view, name='blog home'),
]
