from django.shortcuts import render
from .models import *

# Create your views here.
def about (request):
    return render(request, 'core/about.html')