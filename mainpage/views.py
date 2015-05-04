from django.shortcuts import render
from django.views import generic
from . import models
from django.http import HttpResponse
from django.template import RequestContext, loader


def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def about(request):
    return HttpResponse("This is my about page")