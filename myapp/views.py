from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages


# Create your views here.

def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def blogs(request):
    return render(request, "blogs.html")

def contact(request):
    return render(request, "contact.html")

def faq(request):
    return render(request, "faq.html")
