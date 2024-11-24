from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def index(request):

    return render(request, 'main/index.html')


def page(request):
    return render(request, 'main/page.html')


def page2(request):
    return render(request, 'main/page2.html')