from django.shortcuts import render
from django.views import generic
from . import models
from django.http import HttpResponse


class BlogIndex(generic.ListView):
    queryset = models.Entry.objects.published()
    template_name = "blog/blog.html"
    paginate_by = 3

class BlogDetail(generic.DetailView):
    model = models.Entry
    template_name = "blog/post.html"

class TagIndex(generic.ListView):
    template_name = 'blog/blog.html'
    paginate_by = 3
    
    def get_queryset(self):
        slug = self.kwargs['slug']
        tag = models.Tag.objects.get(slug=slug)
        results = models.Entry.objects.filter(tags=tag)
        return results
