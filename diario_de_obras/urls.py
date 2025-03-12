from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
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
    path('api/v1/', include('core.urls_api')),
    path("listar_obras/", listar_obras, name="listar_obras"),
    path("cadastrar_obras/", cadastrar_obras, name="cadastrar_obras"),
    path("editar_obra/<int:id>/", editar_obra, name="editar_obra"),
    path("excluir_obra/<int:id>/", excluir_obra, name="excluir_obra"),
    path("revisar_obra/<int:id>/", revisar_obra, name="revisar_obra"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
