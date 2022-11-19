from django import forms

from .models import Transaction, Entry

class TransactionForm(forms.ModelForm):
  class Meta:
    model = Transaction
    fields = ['text']
    labels = {'text':''}

class EntryForm(forms.ModelForm):
  class Meta:
    model = Entry
    fields = ['merchant', 'description', 'transaction_amount']
    labels = {'merchant':'merchant', 'description':'description', 'transaction_amount':'transaction_amount'}
    
