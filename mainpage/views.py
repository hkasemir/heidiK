from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic.base import TemplateView
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

class GameView(TemplateView):
    template_name = 'mainpage/tictactoe.html'
