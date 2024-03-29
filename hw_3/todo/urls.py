from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static

from .views import todos_page_view, get_todo_details, get_index_page, delete_todo

urlpatterns = [
    path('add/', todos_page_view),
    path('todos/<int:pk>', get_todo_details),
    path('todos/', get_index_page),
    path('todo/<int:pk>/delete', delete_todo)
]
