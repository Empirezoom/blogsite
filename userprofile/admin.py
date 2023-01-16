from django.contrib import admin
from . models import *

# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'first_name', 'last_name', 'phone', 'email', 'pix','agreement']





admin.site.register(Customer,CustomerAdmin)