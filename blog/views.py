from django.shortcuts import render
from datetime import datetime
from .models import Blog

blogs = Blog.objects.all()
context = {
    'datetime_now': datetime.now().strftime("Today: %d-%m-%Y  |  time: %H:%M"),
    'blogs': blogs,
}


# Create your views here.
def blog_home_view(request):
    return render(request, 'blog/blog_home.html', context)


def blog_individual(request):
    url_path = request.path
    parts = url_path.split('/')
    last_part = parts[-2] if parts[-1] == '' else parts[-1]
    for item in blogs:
        if item.title == last_part:
            context1 = {
                'blog': item,
            }
            return render(request, 'blog/index.html', context1)
