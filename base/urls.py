from django.urls import path
from django.urls.resolvers import URLPattern
from django.views.generic.edit import DeleteView
from .views import CustomLoginVew, RegisterPage, TaskDetail, TaskList, TaskCreate, TaskUpdate, DeleteView
from django.contrib.auth.views import LogoutView

urlpatterns = [ 
    path('login/', CustomLoginVew.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),
    path('', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
    path('task-create/', TaskCreate.as_view(), name='task-create'),
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name='task-update'),
    path('task-delete/<int:pk>/', DeleteView.as_view(), name='task-delete'),

]