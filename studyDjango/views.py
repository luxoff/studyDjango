from django.http.request import *
from django.http.response import *


def hello(request):
    return HttpResponse('<h1>Hello World!</h1>')
