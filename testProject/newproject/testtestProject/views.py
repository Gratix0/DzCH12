from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'testtestProject/index.html')

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


