from django.urls import path

from dashboard.models import Homework
from .import views

urlpatterns = [
    path('home_authenticated', views.home_authenticated, name = "home_authenticated"),   
    path('', views.home_not_authenticated, name = "home_not_authenticated"),   
    path('notes', views.NoteCreateView.as_view(), name = "notes"),    
    path('display_notes', views.NoteDisplayView.as_view(), name = "display_notes"),
    path('note_detail/<int:pk>', views.NoteDetailView.as_view(), name = "note_detail"),
    path('update_note/<int:pk>', views.NoteUpdateView.as_view(), name = "update_note"),    
    path('delete_note/<int:pk>', views.NoteDeleteView.as_view(), name = "delete_note"),    
    path('homework', views.HomeworkCreateView.as_view(), name = "homework"), 
    path('display_homework', views.HomeworkDisplayView.as_view(), name = "display_homework"),   
    path('homework_detail/<int:pk>', views.HomeworkDetailView.as_view(), name = "homework_detail"),
    path('update_homework/<int:pk>', views.HomeworkUpdateView.as_view(), name = "update_homework"),
    path('delete_homework/<int:pk>', views.HomeworkDeleteView.as_view(), name = "delete_homework"), 
]
