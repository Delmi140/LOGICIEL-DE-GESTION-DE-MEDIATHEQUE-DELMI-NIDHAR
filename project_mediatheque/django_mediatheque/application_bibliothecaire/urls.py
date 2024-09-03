from application_bibliothecaire import views

from django.urls import path

urlpatterns = [

    path('', views.listeMembre),


]
