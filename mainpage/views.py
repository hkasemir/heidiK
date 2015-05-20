from django.shortcuts import render, get_object_or_404
from django.views import generic
from . import models


class IndexView(generic.ListView):
    template_name = 'mainpage/index.html'
    context_object_name = 'content_object_list'
    
    def get_queryset(self):
        return models.MainContent.objects.filter(page="index")

class AboutView(generic.ListView):
    template_name = 'mainpage/index.html'
    context_object_name = 'content_object_list'
    
    def get_queryset(self):
        return models.MainContent.objects.filter(page="about")
