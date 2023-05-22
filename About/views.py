from django.shortcuts import render

# Create your views here.
def biography(response):
    return render(response,'About/About.html')