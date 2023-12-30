from django.shortcuts import render
from .models import Car,Model,Make
# Create your views here.

def index(request):
    cars =Car.objects.all()
    models = Model.objects.all()
    makes = Make.objects.all()
    context = {'cars':cars,'models':models,'makes':makes}
    return render(request,'index.html',context)