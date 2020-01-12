from django.shortcuts import render
from django.http import HttpResponse
from app1.models import Student
# Create your views here.
def index(request):
    if (request.method == "POST"):
        name = request.POST.get('name')
        age = request.POST.get('age')
        Class = request.POST.get('Class')

        s=Student(name=name,age=age,Class=Class)
        s.save()
    return render(request,'app1/index.html')
def home(request):
    return HttpResponse('django is a framework')