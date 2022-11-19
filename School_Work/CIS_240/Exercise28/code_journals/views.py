from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Topic
from .forms import TopicForm, EntryForm

def index(request):
  """The home page for Code Journal"""
  return render(request, 'code_journals/index.html')

def topics(request):
  """Show all topics"""
  topics = Topic.objects.order_by('date_added')
  context = {'topics': topics}
  return render(request, 'code_journals/topics.html', context)

def topic(request, topic_id):
  """Show a single topic and all its entries"""
  topic = Topic.objects.get(id=topic_id)
  entries = topic.entry_set.order_by('-date_added')
  context = {'topic': topic, 'entries': entries}
  return render(request, 'code_journals/topic.html', context)

def new_topic(request):
  """Add a new topic."""
  if request.method != 'POST':
    #No data submitted; create a blank form.
    form = TopicForm()
  else:
    #post data submitted; process data
    form = TopicForm(data=request.POST)
    if form.is_valid():
      form.save()
      return HttpResponseRedirect(reverse('code_journals:topics'))

  context = {'form': form}
  return render(request, 'code_journals/new_topic.html', context)

def new_entry(request, topic_id):
  """add a new entry for a particular topic."""
  topic = Topic.objects.get(id=topic_id)

  if request.method !='POST':
    #no data submitted; create a blank form.
    form = EntryForm()
  else:
    #POST data submitted; process data.
    form = EntryForm(data=request.POST)
    if form.is_valid():
      new_entry = form.save(commit=False)
      new_entry.topic = topic
      new_entry.save()
      return HttpResponseRedirect(reverse('code_journals:topic', args=[topic.id]))

  context = {'topic':topic, 'form': form}
  return render(request, 'code_journals/new_entry.html', context)