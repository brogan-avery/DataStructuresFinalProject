from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('editList/', views.editList, name='editList'),
    path('updateBudget/', views.updateBudget, name='updateBudget'),
]