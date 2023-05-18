from django.shortcuts import render
from .models import Person

# Create your views here.

def index(request):
    
    person = Person.objects.order_by('name')
    context = {'name': person}

    return render(request, 'testtestProject/index.html', context)

def about(request):
    return render(request, 'testtestProject/about.html')

def contakts(request):
    return render(request, 'testtestProject/contakts.html')

def pinkipig(request):


    return render(request, 'testtestProject/pinkipig.html')

def switch(request):
    return render(request, 'testtestProject/switch.html')

def tikets(request):
    return render(request, 'testtestProject/tikets.html')


