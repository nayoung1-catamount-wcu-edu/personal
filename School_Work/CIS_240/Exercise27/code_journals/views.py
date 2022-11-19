from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Topic
from .forms import TopicForm

def index(request):
  return render(request, 'code_journals/index.html')

def topics(request):
  topics = Topic.objects.order_by('date_added')
  context = {'topics': topics}
  return render(request, 'code_journals/topics.html', context)

def topic(request, topic_id):
  topic = Topic.objects.get(id=topic_id)
  entries = topic.entry_set.order_by('-date_added')
  context = {'topic': topic, 'entries': entries}
  return render(request, 'code_journals/topic.html', context)

def new_topic(request):
  if request.method != 'POST':
    form = TopicForm()
  else:
    form = TopicForm(data=request.POST)
    if form.is_valid():
      form.save()
      return HttpResponseRedirect(reverse('code_journals:topics'))

  context = {'form': form}
  return render(request, 'code_journals/new_topic.html', context)