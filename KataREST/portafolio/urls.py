from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addUser/', views.addUser, name='addUser'),
    path('userAuth/', views.userAuth, name='userAuth'),
    path('editUser/', views.editUser, name='editUser')
]
