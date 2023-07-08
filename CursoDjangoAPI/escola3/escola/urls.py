from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/v1/', include('cursos.urls')),
    path('admin/', admin.site.urls),
    path('auth/', include('rest_framework.urls')),
]