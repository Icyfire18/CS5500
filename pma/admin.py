from django.contrib import admin

# Register your models here.
from .models import Museum, Usage

admin.site.register(Museum)
admin.site.register(Usage)