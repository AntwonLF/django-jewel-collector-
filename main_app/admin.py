from django.contrib import admin
# import your models here
from .models import Jewels, Cleaning

# Register your models here.
admin.site.register(Jewels)
admin.site.register(Cleaning)