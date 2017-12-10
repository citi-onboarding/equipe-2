from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import *
from .forms import *

# Create your views here.
def home (request):
    context = dict()
    context["cars"] = Car.objects.filter(Availability=True)
    return render(request, 'core/index.html', context)


def cars (request):
    context = dict()
    context["cars"] = Car.objects.filter(Availability=True)
    return render(request, 'core/cars.html', context)


def about (request):
    return render(request, 'core/about.html')


def signin (request):
    pass


def signup (request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect(home)
    else:
        form = SignUpForm()
    return render(request, 'core/register.html', {'form': form})


@login_required(login_url='core/login.html')
def rentProfile (request):
    context = dict()
    context["user"] = request.User
    
    if Contract.objects.all() is not None:
        context["rents"] = Contract.objects.filter(UserID=request.User.username).order_by('DateContract')[:4]
        context["currentRent"] = Contract.objects.filter(UserID=request.User.username).order_by('DateContract').filter(Active=True).first()
    
    return render(resquest, 'core/rent-profile.html', context)


@login_required(login_url='core/login.html')
def tenantProfile (request):
    pass