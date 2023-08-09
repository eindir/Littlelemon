from django.contrib import admin
from .models import Booking, Menu

# Register your models here.
# Permits access to manage your models in the admin site by logging in with a superuser account.
admin.site.register(Booking)
admin.site.register(Menu)