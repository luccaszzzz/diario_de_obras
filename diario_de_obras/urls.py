from django.contrib import admin
from django.urls import path
from core.views import login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login, name='login'),
]
