from django.contrib import admin
from .models import Vehicle, Dealership, Advisor, Service


admin.site.register(Vehicle)
admin.site.register(Dealership)
admin.site.register(Advisor)
admin.site.register(Service)
