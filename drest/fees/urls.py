from django.contrib import admin
from django.urls import path
from .views import fees_django

urlpatterns = [
    path('admin/', admin.site.urls),
    path('first/',fees_django),

]