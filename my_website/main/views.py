from django.shortcuts import render
# from django.http import HttpResponse

from my_website.settings import MY_WEBSITE_NAME


def home(request):
    context = {'my_website_name': MY_WEBSITE_NAME, 'title': 'Home'}
    return render(request, 'main/home.html', context)


def about(request):
    context = {'my_website_name': MY_WEBSITE_NAME, 'title': 'About'}
    return render(request, 'main/about.html', context)
