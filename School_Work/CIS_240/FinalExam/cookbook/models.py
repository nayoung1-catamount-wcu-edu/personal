from django.db import models

class MealCategory(models.Model):
  categoryType= models.CharField(max_length=200)
  dateAdded = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.categoryType

class Recipe(models.Model):
  mealCategory = models.ForeignKey(MealCategory, on_delete=models.CASCADE)
  recipeName = models.CharField(max_length=200)
  ingredients = models.TextField()
  dateAdded = models.DateTimeField(auto_now_add=True)

  class Meta:
    verbose_name_plural = 'recipes'

  def __str__(self):
    return self.recipeName