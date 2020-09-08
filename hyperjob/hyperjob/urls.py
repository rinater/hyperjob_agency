"""hyperjob URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include, re_path

from hyperjob import views
from hyperjob.views import menu, MyLogOutView, MyHome
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', menu, name='menu'),
    path('resumes/', include('resume.urls')),
    path('vacancies/', include('vacancy.urls')),
    path('login', views.MyLoginView.as_view()),
    path('login/', RedirectView.as_view(url='/login')),
    path('signup', views.MySignupView.as_view()),
    path('signup/', RedirectView.as_view(url='/signup')),
    path("logout/", MyLogOutView.as_view(), name="logout"),
    path('home/', MyHome.as_view(), name='home'),
    path('resume/', include('resume.urls')),
    path('vacancy/', include('vacancy.urls')),
]
'''
    re_path('signup/', views.SignUpView.as_view()),
    re_path('login/', views.LoginView.as_view()),
    re_path('logout/', views.LogoutView.as_view()),
'''
