from django.shortcuts import render, redirect
from django.http import HttpResponse, request, HttpResponseRedirect, HttpResponseForbidden
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic.base import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import AuthenticationForm, LoginView, LogoutView
from django.views.generic import CreateView, TemplateView
from hyperjob.forms import MyForm
from resume.models import Resume
from vacancy.models import Vacancy
from django.core.exceptions import PermissionDenied


def menu(request):
    return render(request, 'menu/main.html')


class MyHome(View):
    def __init__(self):
        self.all_resumes = Resume.objects.all()
        self.all_vacancies = Vacancy.objects.all()

    def get(self, request, *args, **kwargs):
        f = MyForm()
        context = {'resumes': self.all_resumes, 'vacancies': self.all_vacancies, 'is_staff': request.user.is_staff,
                   'form': f, 'is_authenticated': request.user.is_authenticated}
        return render(request, 'menu/home.html', context=context)

    def post(self, request, *args, **kwargs):
        f = MyForm(data=request.POST)
        user = request.user
        context = {'resumes': self.all_resumes, 'vacancies': self.all_vacancies, 'is_staff': request.user.is_staff,
                   'form': f, }
        if not user.is_authenticated:
            raise PermissionDenied
        if f.is_valid():
            description = f.cleaned_data['description']
            if user.is_staff:
                v = Vacancy(description=description, author=user)
                v.save()
            else:
                r = Resume(description=description, author=user)
                r.save()
        # redirect('/')
        return render(request, 'menu/home.html', context=context)

    def index(self, request, *args, **kwargs):
        context = {'resumes': self.all_resumes, 'vacancies': self.all_vacancies, 'is_staff': request.user.is_staff, }
        return render(request, 'menu/home.html', context=context)


class MyLoginView(LoginView):
    form_class = AuthenticationForm
    redirect_authenticated_user = True
    template_name = "menu/login.html"


class MySignupView(CreateView):
    form_class = UserCreationForm
    success_url = "/login"
    template_name = "menu/signup.html"


class MyLogOutView(LogoutView):
    pass


'''
class SignUpView(View):
    def get(self, request, *args, **kwargs):
        f = UserCreationForm()
        return render(request, 'signup.html', context={'form': f})

    def post(self, request, *args, **kwargs):
        f = UserCreationForm(request.POST)
        if f.is_valid():
            User.objects.create_user(username=f.cleaned_data['username'], password=f.cleaned_data['password1'])
            return redirect('/')
        return render(request, 'signup.html', {'form': f})


class LoginView(View):
    def get(self, request, *args, **kwargs):
        f = AuthenticationForm()
        return render(request, 'menu/login.html', context={'form': f})

    def post(self, request, *args, **kwargs):
        f = AuthenticationForm(data=request.POST)
        if f.is_valid():
            user = authenticate(username=f.cleaned_data['username'], password=f.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                print("The username and password were incorrect.")
        return render(request, 'login.html', {'form': f})


class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('/')
'''
