from django.shortcuts import render
from datetime import datetime

context = {
    'datetime_now' : datetime.now().strftime("Today: %d-%m-%Y  |  time: %H:%M")
}
# Create your views here.
def home_view(request):
    return render(request, 'pages/home.html', context)


def about_view(request):
    return render(request, 'pages/about.html', context)


def contact_view(request):
    return render(request, 'pages/contact.html', context)
