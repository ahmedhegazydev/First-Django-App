from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

# def home(request):
    # return HttpResponse("<h1>Hello World</h1>")
#     return HttpResponse("Hello World")

def home(request):
    return render(request, "home.html", {'name': "Ahmed"})
    # return render(request, "home.html")

