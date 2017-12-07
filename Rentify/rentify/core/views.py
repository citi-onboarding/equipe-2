from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *

# Create your views here.
def home (request):
    context = dict()
    context["cars"] = Car.objects.filter(Availability=True)
    return render(request, 'core/index.html', context)


def ourCars (request):
    pass


def about (request):
    return render(request, 'core/about.html')
    

def signIn (request):
    pass


def signUp (request):
    pass

@login_required(login_url='core/login.html')
def rentProfile (request):
    context = dict()
    pass


def tenantProfile (request):
    pass