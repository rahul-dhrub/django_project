from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def homepage(request):
    return HttpResponse("Wow this is a <strong>awesome<strong>tutorial!!")
