from django.contrib import admin

# Register your models here.
from .models import Model,Make,BodyType,Car,Image


class CarAdmin(admin.ModelAdmin):
    list_display=('model','make','body','isAvailable','isFeatured','locationValue','mileage','engineSize','drive','transmission','horsePower','acceleration','fuelType')

class MakeAdmin(admin.ModelAdmin):
    list_display=('name','image')
    
# class ModelAdmin(admin.ModelAdmin):
#     list_display=('name')
    
# class BodyTypeAdmin(admin.ModelAdmin):
#     list_display=('name')

admin.site.register(Model)
admin.site.register(Make,MakeAdmin)
admin.site.register(BodyType)
admin.site.register(Car)
admin.site.register(Image)