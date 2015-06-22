from django.conf.urls import url, patterns, include
from django.views.generic.base import TemplateView
from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name="index"),
    url(r'^about/$', views.AboutView.as_view(), name="about"),
    url(r'^game/tictactoe$', views.GameView.as_view(), name="game"),
    ]