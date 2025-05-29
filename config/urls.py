"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, re_path, include

from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

from django.conf.urls import handler400, handler403, handler404, handler500

from .errors import custom_400_view, custom_401_view, custom_403_view, custom_404_view, custom_500_view


urlpatterns = [
    path('furni/', admin.site.urls),

    path('unauthorized/', custom_401_view, name='unauthorized'),

    path('ckeditor/', include('ckeditor_uploader.urls')),

    path('', include('apps.agent.urls')),
    path('', include('apps.contact.urls')),
    path('', include('apps.user.urls')),
    path('', include('apps.blog.urls')),
    path('', include('apps.cart.urls')),
    path('', include('apps.common.urls')),
    path('', include('apps.product.urls')),

    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

handler400 = custom_400_view
handler403 = custom_403_view
handler404 = custom_404_view
handler500 = custom_500_view
