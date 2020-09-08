from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.contrib.auth.models import User
from .models import Resume
from hyperjob.forms import MyForm
from django.core.exceptions import PermissionDenied
from resume.models import Resume
from vacancy.models import Vacancy
from django.http import HttpResponse, request, HttpResponseRedirect, HttpResponseForbidden


# Create your views here.
class ViewResumes(View):
    def get(self, request, *args, **kwargs):
        all_resumes = Resume.objects.all()
        context = {'resumes': all_resumes}
        return render(request, 'resume/all.html', context)


class NewResume(View):
    def get(self, request, *args, **kwargs):
        f = MyForm()
        return render(request, 'resume/new.html', context={'form': f})

    def post(self, request, *args, **kwargs):
        f = MyForm(data=request.POST)
        print(request.POST)
        user = request.user
        if not isinstance(user, User):
            raise PermissionDenied
        if request.user.is_staff:
            raise PermissionDenied
        if request.method == 'POST':

            if f.is_valid():
                description = f.cleaned_data['description']
                r = Resume(description=description, author=user)
                r.save()
            return redirect('/home')
        # return render(request, 'resume/new.html', context={'form': f})
