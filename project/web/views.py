from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    context = {
        'title': 'Tony',
        'top': '"{%url "web-home"%}"',
    }
    return render(request, 'web/home.html', context)


def about(request):
    context = {
        'title': 'About',
    }
    return render(request, 'web/about.html')

def portfolio(request):
    return render(request, 'web/projects.html')

def contact(request):
    return render(request, 'web/contact.html')

