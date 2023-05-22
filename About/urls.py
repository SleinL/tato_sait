from django.urls import path
from About.views import biography

app_name = 'About'
urlpatterns = [
    path('', biography, name='biography'),
]