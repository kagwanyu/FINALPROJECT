from django.shortcuts import render
from django.http import HttpResponse
from .models import Allth

def home(request):
    allth = Allth.objects.all()
    return render(request, 'home.html', {'allth': allth})
