from django.contrib import admin
from .models import Profile,Hood,updates,Businesses,Medicalservices,HealthServices,Adminstration,Post,Comments


# Register your models here.
admin.site.register(Profile)
admin.site.register(HealthServices)
admin.site.register(Hood)
admin.site.register(Post)
admin.site.register(Comments)

admin.site.register(updates)
admin.site.register(Businesses)
admin.site.register(Medicalservices)
admin.site.register(Adminstration)
