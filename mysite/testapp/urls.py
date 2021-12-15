from . import views
from django.urls import path

urlpatterns = [
    path('', views.TaskListView.as_view(), name='home'),
    path('task/<slug:slug>/', views.TaskDetailView.as_view(), name='task_detail'),
    path('add_task/', views.AddTaskView.as_view(), name='add_task'),
    path('edit_task/<slug>/', views.EditTaskView.as_view(), name='edit_task'),
    path('delete_task/<slug>/', views.DeleteTaskView.as_view(), name='delete_task'),
    path('about/', views.AboutPageView.as_view(), name='about'),
    path('policy/', views.PolicyPageView.as_view(), name='policy'),
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.RegisterUser.as_view(), name='register'),
]