from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render

def test(request):
    return HttpResponse("hello world")


def index(request):
    return render(request, 'index.html', '')