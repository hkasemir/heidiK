from django.contrib import admin
from . import models


class MainContentAdmin(admin.ModelAdmin):
    list_display = ("header", "page")

admin.site.register(models.MainContent, MainContentAdmin)
