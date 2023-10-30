
from django.shortcuts import render


# Create your views here.

def about(request):
    return render(request, 'about.html', {'navbar': 'about'})


def classes(request):
    return render(request, 'classes.html',{'navbar': 'classes'}),

def contact(request):
    return render(request, 'contact.html',{'navbar': 'contact'}),

def add(request):
    return render(request, 'add.html', {'navbar': 'add'})



