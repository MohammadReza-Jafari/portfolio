from django.shortcuts import render
from .models import Job

# Create your views here.


def home(request):
    jobList=Job.objects
    return render(request,'jobs/home.html',{'jobs':jobList})