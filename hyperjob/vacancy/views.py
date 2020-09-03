from django.shortcuts import render, HttpResponse
from .models import Vacancy


# Create your views here.
def index(request):
    all_vacancies = Vacancy.objects.all()
    context = {'vacancies': all_vacancies}
    return render(request, 'vacancy/all.html', context)
