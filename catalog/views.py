from django.shortcuts import render


# Create your views here.


def index(request, *args, **kwargs):
    return render(request, 'catalog/index.html')


def contacts(request, *args, **kwargs):
    return render(request, 'catalog/contacts.html')
