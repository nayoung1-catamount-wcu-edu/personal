from django.contrib import admin

# Register your models here
from cookbook.models import MealCategory, Recipe

admin.site.register(MealCategory)
admin.site.register(Recipe)