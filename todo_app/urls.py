from django.urls import path

from todo_app import views

app_name = 'todo_normal'

urlpatterns = [
    path('todo_list', views.todo_list, name='todo_list'),
    path('todo_add', views.todo_add, name='todo_add'),
    path('todo_delete/<int:id>/', views.todo_delete, name='todo_delete'),
    path('todo_update/<int:id>/', views.todo_update, name='todo_update'),
]
