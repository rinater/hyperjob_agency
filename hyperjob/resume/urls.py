from django.urls import path
from .import views
from .views import NewResume, ViewResumes
app_name = 'resume'
urlpatterns = [
    path('', ViewResumes.as_view(), name='index'),
    path('new/', NewResume.as_view(), name='new'),
]
