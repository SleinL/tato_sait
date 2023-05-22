from django.shortcuts import render

# Create your views here.
def blog_func(respouns):
    return render(respouns,'Blog/Blog.html')
