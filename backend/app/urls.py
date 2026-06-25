from django.contrib import admin
from django.urls import path, include

from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'health/', views.health, name="health"),
    path(r'api/', include('api.urls'), name="api"),
]
