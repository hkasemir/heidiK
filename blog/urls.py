from django.conf.urls import url
from . import views, feed

urlpatterns = [
    url(r'^$', views.BlogIndex.as_view(), name="blog"),
    url(r'^tag/(?P<slug>\S+)$', views.TagIndex.as_view(), name="tag_index"),
    url(r'^feed/$', feed.LatestPosts(), name="feed"),
    url(r'^(?P<slug>\S+)$', views.BlogDetail.as_view(),
        name="entry_detail"),
]
