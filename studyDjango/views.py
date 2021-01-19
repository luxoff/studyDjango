from django.http.request import *
from django.http.response import *
from django.shortcuts import render


def hello(request):
    return render(request, 'base.html')
