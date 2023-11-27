from django.contrib import admin

# Register your models here.
from .models import Museum, Usage, Weather

admin.site.register(Museum)
admin.site.register(Usage)
admin.site.register(Weather)