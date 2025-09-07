from django.urls import path
from .views import blog_individual
from .models import Blog

blogs = Blog.objects.all()
urlpatterns = [
    path(f"{blog.title.replace(' ', '-')}/", blog_individual, name=blog.title) for blog in blogs
]
