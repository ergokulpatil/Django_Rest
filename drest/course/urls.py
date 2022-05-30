from django.contrib import admin
from django.urls import path
from .views import learn_django,print_string,index
urlpatterns = [
    path('',index),
    path('learn',learn_django),
    path('print',print_string)
]
