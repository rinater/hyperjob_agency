from django.urls import path
from .import views
from .views import NewVacancy, ViewVacancies
app_name = 'resume'
urlpatterns = [
    path('', ViewVacancies.as_view(), name='index'),
    path('new/', NewVacancy.as_view(), name='new'),
]
