from django.contrib import admin
from .models import all_classes

# Register your models here.
for model in all_classes:
    admin.site.register(model)
