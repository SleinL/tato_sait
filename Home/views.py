from django.shortcuts import render

# Create your views here.
def index(respouns):
    return render(respouns, 'Home/Homes.html')