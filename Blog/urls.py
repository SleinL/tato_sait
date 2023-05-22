from django.urls import path
from Blog.views import blog_func

app_name = 'Blog'
urlpatterns = [
    path('Blog',blog_func, name='blog_func'),
]