from django.contrib import admin
from .models import Allth

# Register your models here.
class AllthAdmin (admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity')

admin.site.register(Allth, AllthAdmin) 
