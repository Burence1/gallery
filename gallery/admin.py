from django.contrib import admin
from .models import Location,Category,Images


# Register your models here.
admin.site.register(Location)
admin.site.register(Images)
admin.site.register(Category)