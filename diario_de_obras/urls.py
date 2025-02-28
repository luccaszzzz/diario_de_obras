from django.contrib import admin
from django.urls import path
from core.views import login, listar_obras, cadastrar_obras

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login, name='login'),
    path('home/', listar_obras, name='listar_obras'),
    path('cadastrar_obras/', cadastrar_obras, name='cadastrar_obras'),
]
