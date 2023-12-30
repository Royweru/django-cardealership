from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='home'),
    path('new/',views.create_car,name='new')
]