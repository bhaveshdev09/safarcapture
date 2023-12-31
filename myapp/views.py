from django.shortcuts import render, redirect,HttpResponse
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
from django_core.settings import EMAIL_HOST_USER
from myapp.models import *


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

def destination(request):
    return render(request, "destination.html")

def thankyou(request):
    return render(request, "thankyou.html")

def query_form(request):
    if request.method == "POST":
        print(request.POST)
        instance = Query() # instance of model
        instance.full_name = request.POST.get("full_name")
        instance.phone_number = request.POST.get("phone_number")
        instance.email = request.POST.get("email")
        instance.adult_count = int(request.POST.get("adult_count"))
        instance.child_count = int(request.POST.get("child_count"))
        instance.message =request.POST.get("message")
        instance.destination = request.POST.get("destination")
        instance.save()
        messages.success(request, 'Thanks for contacting SufferCapture !')
        
        #email process starts from here
        try:
            subject = "Thanks for contacting SufferCapture !"
            # text_content = "This is an important message."
            html_content = """<p> Dear Customer, <strong>Thanks for contacting SufferCapture</strong> <br> Will connect back to you soon.</p>"""
            msg = EmailMultiAlternatives(subject, "" , from_email=EMAIL_HOST_USER ,to= [request.POST.get("email")], bcc=["sagavekarom@zohomail.in"])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
        except:
            return redirect('index' )   

        return redirect('thankyou')
    else:
        return redirect('index')
        
def contactus(request):
    if request.method == "POST":
        print(request.POST)
        instance = Contact() 
        instance.fname = request.POST.get("first_name")
        instance.lname = request.POST.get("last_name")
        instance.email = request.POST.get("email")
        instance.phone_number = request.POST.get("phone")
        instance.message =request.POST.get("comments")
        instance.save()
        
        #email process starts from here
        try:
            subject = "Thanks for contacting SufferCapture !"
            # text_content = "This is an important message."
            html_content = """<p> Dear Customer, <strong>Thanks for contacting SufferCapture</strong> <br> Will connect back to you soon.</p>"""
            msg = EmailMultiAlternatives(subject, "" , from_email=EMAIL_HOST_USER ,to= [request.POST.get("email")], bcc=["sagavekarom@zohomail.in"])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
        except:
            return redirect('index' )   

        return redirect('thankyou')
    else:
        return redirect('index')


        
#temp forms-->
def destination_admin(request):
    if request.method == "POST":
        print(request.POST, request.user)
        instance = Destination()
        instance.name = request.POST.get("destination_name")
        instance.state = request.POST.get("destination_state")
        instance.description = request.POST.get("destination_description") 
        instance.map_link = request.POST.get("destination_map_link")
        instance.save()
        return HttpResponse("form posted")
    else:  
        return render(request, "0_destination_form.html")


    
