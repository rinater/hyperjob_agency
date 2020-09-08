from django.shortcuts import render, HttpResponse, redirect
from .models import Vacancy
from hyperjob.forms import MyForm
from django.core.exceptions import PermissionDenied
from django.views.generic.base import View
from django.http import HttpResponse, request, HttpResponseRedirect, HttpResponseForbidden
from django.contrib.auth.models import User
# Create your views here.
class ViewVacancies(View):
    def get(self, request, *args, **kwargs):
        all_vacancies = Vacancy.objects.all()
        context = {'vacancies': all_vacancies}
        return render(request, 'vacancy/all.html', context)


class NewVacancy(View):
    def get(self, request, *args, **kwargs):
        f = MyForm()
        return render(request, 'vacancy/new.html', context={'form': f})

    def post(self, request, *args, **kwargs):
        f = MyForm(data=request.POST)
        user = request.user
        if not user.is_staff:
            raise PermissionDenied
        if not isinstance(user, User):
            raise PermissionDenied
        if request.method == 'POST':
            if f.is_valid():
                description = f.cleaned_data['description']
                v = Vacancy(description=description, author=user)
                v.save()
            return redirect('/home')
            #return render(request, 'vacancy/new.html', context={'form': f})
