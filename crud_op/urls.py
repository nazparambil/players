from django.urls import path
from .import views

urlpatterns=[
    path('',views.index),
    path('displayall',views.displayall),
    path('search',views.search),
    path('addnewplayers',views.addnewplayers),
    path('deleteplayer',views.deleteplayer)



]
