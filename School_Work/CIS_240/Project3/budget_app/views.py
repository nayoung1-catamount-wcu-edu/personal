from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Transaction
from .forms import TransactionForm

#Create your views here.
def index(request):
  return render(request, 'budget_app/index.html')

def transactions(request):
  transactions = Transaction.objects.order_by('date_added')
  context = {'transactions': transactions}
  return render(request, 'budget_app/transactions.html', context)

def transaction(request, transaction_id):
  transaction = Transaction.objects.get(id=transaction_id)
  entries = transaction.entry_set.order_by('-date_added')
  context = {'transaction': transaction, 'entries': entries}
  return render(request, 'budget_app/transaction.html', context)

def new_transaction(request):
  if request.method != 'POST':
    form = TransactionForm()
  else:
    form = TransactionForm(data=request.POST)
    if form.is_valid():
      form.save()
      return HttpResponseRedirect(reverse('budget_app:transactions'))

  context = {'form': form}
  return render(request, 'budget_app/new_transaction.html', context)