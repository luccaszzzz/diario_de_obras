from django.contrib import admin
from django.urls import path
from core.views import (
    login,
    listar_obras,
    cadastrar_obras,
    editar_obra,
    excluir_obra,
    revisar_obra,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", login, name="login"),
    path("listar_obras/", listar_obras, name="listar_obras"),
    path("cadastrar_obras/", cadastrar_obras, name="cadastrar_obras"),
    path("editar_obra/<int:id>/", editar_obra, name="editar_obra"),
    path("excluir_obra/<int:id>/", excluir_obra, name="excluir_obra"),
    path("revisar_obra/<int:id>/", revisar_obra, name="revisar_obra"),
]
