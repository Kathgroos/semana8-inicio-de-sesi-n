from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include

# Importa la vista de index que has definido
#from .views import index

# Importa el módulo redirect desde django.shortcuts
from django.shortcuts import redirect

# Define la vista de redirección para la página de inicio
def index(request):
    return redirect('accounts/')  # Redirige a la URL de accounts/

# Define las URLs de la aplicación
urlpatterns = [
    # Redirige la página de inicio a /accounts/
    path("", index, name="index"),

    # URL para acceder al panel de administración de Django
    path('admin/', admin.site.urls),

    # URLs de la aplicación 'tasks'
    path('tasks/', include('tasks.urls')),

    # URLs de la aplicación 'accounts'
    path('accounts/', include('accounts.urls')),
]

# Configuración para servir archivos estáticos durante el desarrollo
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)











"""
# Definición de las URLs de la aplicación
urlpatterns = [
    # Redirección de la página de inicio a /accounts/
    path("", RedirectView.as_view(url="accounts/", permanent=False), name="index"),

    # URL para acceder al panel de administración de Django
    path('admin/', admin.site.urls),

    # URLs de la aplicación 'tasks'
    path('tasks/', include('tasks.urls')),

    # URLs de la aplicación 'accounts'
    path('accounts/', include('accounts.urls')),
]

# Configuración para servir archivos estáticos durante el desarrollo
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)"""












"""from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import RedirectView


urlpatterns = [
    path("", RedirectView.as_view(url="accounts/", permanent=False), name="index"),
    path('admin/', admin.site.urls),
    path('tasks/', include('tasks.urls')),
    path('accounts/', include('accounts.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)"""