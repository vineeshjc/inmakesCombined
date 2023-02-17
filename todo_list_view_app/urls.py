from django.urls import path

from todo_list_view_app import views

app_name = 'todo_class'

urlpatterns = [
    path('todo_add', views.todo_add, name='todo_add'),
    path('todo_list', views.todo_list.as_view(), name='todo_list'),
    path('todo_details/<int:pk>/', views.todo_details.as_view(), name='todo_details'),
    path('todo_delete/<int:pk>/', views.todo_delete.as_view(), name='todo_delete'),
    path('todo_update/<int:pk>/', views.todo_update.as_view(), name='todo_update')
]
