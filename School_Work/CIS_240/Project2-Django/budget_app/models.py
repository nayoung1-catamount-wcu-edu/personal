from django.db import models

# Create your models here.
class Transaction(models.Model):
  TransactionType = models.CharField(max_length=200)
  date_added = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.TransactionType