from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Transaction, Entry
from .forms import TransactionForm, EntryForm

#Create your views here.
def index(request):
  #The home page for Code Journals.
  return render(request, 'budget_app/index.html')

def transactions(request):
  #Show all topics.
  transactions = Transaction.objects.order_by('date_added')
  context = {'transactions': transactions}
  return render(request, 'budget_app/transactions.html', context)

def transaction(request, transaction_id):
  #Show a single topic and all its entries.
  transaction = Transaction.objects.get(id=transaction_id)
  entries = transaction.entry_set.order_by('-date_added')
  context = {'transaction': transaction, 'entries': entries}
  return render(request, 'budget_app/transaction.html', context)

def new_transaction(request):
  #add a new topic.
  if request.method != 'POST':
    #no data submitted; create a blank form.
    form = TransactionForm()
  else:
    #post data sumitted; process data.
    form = TransactionForm(data=request.POST)
    if form.is_valid():
      form.save()
      return HttpResponseRedirect(reverse('budget_app:transactions'))

  context = {'form': form}
  return render(request, 'budget_app/new_transaction.html', context)

def new_entry(request, transaction_id):
  #add a new entry for a particular topic.
  transaction = Transaction.objects.get(id=transaction_id)

  if request.method !='POST':
    #no data submitted; create a blank form.
    form = EntryForm()
  else:
    #POST data submitted; process data.
    form = EntryForm(data=request.POST)
    if form.is_valid():
      new_entry = form.save(commit=False)
      new_entry.transaction = transaction
      new_entry.save()
      return HttpResponseRedirect(reverse('budget_app:transaction', args=[transaction_id]))

  context = {'transaction': transaction, 'form': form}
  return render(request, 'budget_app/new_entry.html', context)