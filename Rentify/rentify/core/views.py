from django.shortcuts import render
from .models import *

# Create your views here.
def home (request):
    context = dict()
    context["cars"] = Car.objects.all()

    return render(request, 'core/index.html', context)


def ourCars (request):
    pass


def about (request):
    return render(request, 'core/about.html')
    

def signIn (request):
    pass


def signUp (request):
    pass


def rentProfile (request):
    pass


def tenantProfile (request):
    pass