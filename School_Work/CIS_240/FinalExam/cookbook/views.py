from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import MealCategory
from .forms import MealCategoryForm

#Create your views here.
def index(request):
  return render(request, 'cookbook/index.html')

def mealCategories(request):
  mealCategories = MealCategory.objects.order_by('dateAdded')
  context = {'mealCategories': mealCategories}
  return render(request, 'cookbook/mealCategories.html', context)

def mealCategory(request, mealCategory_id):
  mealCategory = MealCategory.objects.get(id=mealCategory_id)
  recipes = mealCategory.recipe_set.order_by('-dateAdded')
  context = {'mealCategory': mealCategory, 'recipes': recipes}
  return render(request, 'cookbook/mealCategory.html', context)

def new_mealCategory(request):
  if request.method != 'POST':
    form = MealCategoryForm()
  else:
    form = MealCategoryForm(data=request.POST)
    if form.is_valid():
      form.save()
      return HttpResponseRedirect(reverse('cookbook:mealCategories'))

  context = {'form': form}
  return render(request, 'cookbook/new_mealCategory.html', context)