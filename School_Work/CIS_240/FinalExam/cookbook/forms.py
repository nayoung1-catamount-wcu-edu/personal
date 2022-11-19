from django import forms

from .models import MealCategory

class MealCategoryForm(forms.ModelForm):
  class Meta:
    model = MealCategory
    fields = ['categoryType']
    labels = {'categoryType':'categoryType'}