from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Make(models.Model):
    name=models.CharField(max_length=50)
    image = models.ImageField(upload_to='media/images/make', height_field=None, width_field=None, max_length=None)
    
class BodyType(models.Model):
    name= models.CharField(max_length=100)
    image = models.ImageField( upload_to='media/images/body', height_field=None, width_field=None, max_length=None)
    
class Model(models.Model):
     name= models.CharField(max_length=100)
     make = models.ForeignKey(Make,on_delete = models.SET_NULL, null = True)
class Car(models.Model):
    make = models.ForeignKey(Make,on_delete=models.SET_NULL,null=True)
    body = models.ForeignKey(BodyType,on_delete= models.SET_NULL,null=True)
    model = models.ForeignKey(Model,on_delete=models.SET_NULL, null = True)
    mileage= models.IntegerField(default=50000)
    engineSize = models.IntegerField(default=2000)
    drive = models.CharField(max_length=50,default="2WD")
    price = models.IntegerField()
    locationValue = models.CharField(max_length = 2400)
    yearOfManufacture= models.CharField(max_length=20)
    isFeatured= models.BooleanField()
    isAvailable = models.BooleanField()
    transmission = models.CharField(max_length=50)
    horsePower = models.IntegerField()
    acceleration = models.DecimalField(max_digits=5,decimal_places=2)
    fuelType = models.CharField(max_length=50)
    
    
    
class Image(models.Model):
    picture = models.ImageField( upload_to='media/images/cars', height_field=None, width_field=None, max_length=None)
    car = models.ForeignKey(Car,on_delete=models.CASCADE)