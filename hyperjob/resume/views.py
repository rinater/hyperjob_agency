from django.shortcuts import render
from .models import Resume


# Create your views here.
def index(request):
    all_resumes = Resume.objects.all()
    context = {'resumes': all_resumes}
    return render(request, 'resume/all.html', context)
