from django.urls import path
from django.views.decorators.cache import cache_page

from blog.apps import BlogConfig
from blog.views import BlogDetailView

app_name = BlogConfig.name

urlpatterns = [
    path('blog/article/<slug>', cache_page(60)(BlogDetailView.as_view()), name='article'),

]
