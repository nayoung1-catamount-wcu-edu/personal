from django.contrib import admin

# Register your models here
from budget_app.models import Transaction

admin.site.register(Transaction)