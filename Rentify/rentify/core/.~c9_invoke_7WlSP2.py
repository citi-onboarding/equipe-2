from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import *
from .forms import *

# Create your views here.
def home (request):
    context = dict()
    context["cars"] = Car.objects.filter(Availability=True)
    return render(request, 'core/index.html', context)


def ourCars (request):
    context = dict()
    cars = Car.objects.filter(Availability=True)
    
    # Paginator
    paginator = Paginator(cars, 9)
    page = request.GET.get('page', 1)
    context["cars"] = paginator.page(page)
    print(context["cars"].has_other_pages)
    
    return render(request, 'core/ourCars.html', context)


def about (request):
    return render(request, 'core/about.html')


def signin (request):
    print("To PEGANDO!!!!!!")
    if request.method == 'POST':
        print("Verrrrrrrr")
        if form.is_valid():
        if form.is_valid():
            print("Testando se e valido")
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request,user)
                redirect(home)
            else:
                login(request,user)
                redirect(rentProfile)
                
    else:
        form = SignInForm()
    return render(request, 'core/login.html', {'form': form})

def signUp (request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
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