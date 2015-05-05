from django.shortcuts import render, get_object_or_404
from django.views import generic
from . import models


def index(request):
    return render(request, 'mainpage/index.html')

def about(request):
    return render(request, 'mainpage/about.html')