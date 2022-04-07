from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.


def starting_page(request):
    return render(request, "blog/index.html")


def posts(request):
    return render(request, "blog/all-posts.html")


def specific_post(request, post):
    return HttpResponse("specific post " + post)
