"""Defines URL patterns for code_journals."""

from django.urls import path, include

from . import views
app_name = 'code_journals'
urlpatterns = [
  #Home page
  path('', views.index, name='index'),

  #show all topics
  path('topics/', views.topics, name='topics'),

  #detail page for a single topic
  path('topics/<int:topic_id>/', views.topic, name='topic'),

  #page for adding a new topic
  path('new_topic/', views.new_topic, name='new_topic'),

  #page for adding a new entry
  path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),

  #page for editing a new entry
  path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
]