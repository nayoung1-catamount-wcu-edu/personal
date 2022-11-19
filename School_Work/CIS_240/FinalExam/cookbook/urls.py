"""Define URL patterns for cookbook."""

from django.urls import path, include 

from . import views
app_name = 'cookbook'
urlpatterns = [
  #home page
  path('', views.index, name='index'), 

  #show all mealCategories
  path('mealCategories/', views.mealCategories, name='mealCategories'),

  #detail page for single MealCategory
  path('mealCategories/<int:mealCategory_id>/', views.mealCategory, name='mealCategory'),

  #page for adding a new MealCategory
  path('new_mealCategory/', views.new_mealCategory, name='new_mealCategory'),
]