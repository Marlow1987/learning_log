"""URL of app learning_logs"""
from django.urls import path
from . import views

app_name = 'learning_logs'
urlpatterns = [
    #index
    path('',views.index,name='index'),
    #show topics
    path('topics/',views.topics,name='topics'),
    #show specific entry
    path('topics/<int:topic_id>/',views.topic,name='topic'),
    #show page of adding new topic
    path('new_topic/',views.new_topic,name='new_topic'),
    #show page of adding new entry
    path('new_entry/<int:topic_id>/',views.new_entry,name='new_entry'),
    #show page of editing
    path('edit_entry/<int:entry_id>/',views.edit_entry,name='edit_entry'),
]
