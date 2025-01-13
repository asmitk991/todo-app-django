from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('todo/', views.todo, name='todo'),
    path('add/', views.add_task, name='add_task'),
    path('complete/<int:task_id>/', views.mark_as_complete, name='mark_as_complete'),
    path('toggle/<int:task_id>/', views.toggle_task_status, name='toggle_task_status'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
]