from django.shortcuts import render
from django.http import HttpResponse


def menu(request):
    return render(request, 'menu/main.html')
