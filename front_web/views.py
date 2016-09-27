from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render


def test(request):
    return HttpResponse("hello world")


def demo_index(request):
    return render(request, 'demo_index.html', '')


def index(request):
    return render(request, 'index.html', '')