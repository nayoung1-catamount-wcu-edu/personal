from django.contrib import admin

# Register your models here
from budget_app.models import Transaction, Entry

admin.site.register(Transaction)
admin.site.register(Entry)