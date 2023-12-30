from django.shortcuts import render
from .models import Car,Model,Make
from .forms import CarForm
# Create your views here.

def index(request):
    cars =Car.objects.all()
    models = Model.objects.all()
    makes = Make.objects.all()
    context = {'cars':cars,'models':models,'makes':makes}
    return render(request,'index.html',context)


def create_car(request):
    form = CarForm()
    context = {'form':form}
    return render(request,'new-form.html',context)