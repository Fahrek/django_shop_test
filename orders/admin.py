from django.contrib import admin
from .models import OrderLine, Order


# Register your models here.
admin.site.register([Order, OrderLine])  # Los registramos para que aparezcan en el panel de admin
