from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def index(request):
    my_dict = {'insert_me': "Hello Chamath"}
    return render(request, 'header/index.html', context=my_dict)
