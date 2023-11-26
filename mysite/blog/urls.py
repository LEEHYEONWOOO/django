from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.index),
    path('get_BoardList/', views.get_BoardList),
    path('get_BoardDetail/', views.get_BoardDetail),
    path('Board_write/', views.Board_write),
    path('Pass_chk_Submit', views.Pass_chk_Submit),


    



]