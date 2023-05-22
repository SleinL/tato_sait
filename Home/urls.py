from Home.views import index
from django.urls import path
app_name = 'Home'
urlpatterns = [
    path('', index, name='index'),
]