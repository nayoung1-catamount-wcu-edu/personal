"""Define URL patterns for budget_app."""

from django.urls import path, include 

from . import views
app_name = 'budget_app'
urlpatterns = [
  #home page
  path('', views.index, name='index'), 

  #show all transactions
  path('transactions/', views.transactions, name='transactions'),

  #detail page for single transaction
  path('transactions/<int:transaction_id>/', views.transaction, name='transaction'),

  #page for adding a new transaction
  path('new_transaction/', views.new_transaction, name='new_transaction'),
]