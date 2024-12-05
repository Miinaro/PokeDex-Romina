from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pokedex.urls')),  # Redirige a las URLs de la app pokedex
]
