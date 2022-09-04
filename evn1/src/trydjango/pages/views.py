from django.http import HttpResponse
from django.shortcuts import render

def home_view(*args, **kwargs):
    return HttpResponse("<h1> Home </h1>")

def contact_view(request, *args, **kwargs):
    return render(request, "contact.html", {} )
