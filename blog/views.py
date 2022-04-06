from django.http import HttpResponse
from django.shortcuts import render
from django.urls import path, include
# Create your views here.


def starting_page(request):
    return HttpResponse("featured")


def posts(request):
    return HttpResponse("all")


def specific_post(request, post):
    return HttpResponse("specific post " + post)
