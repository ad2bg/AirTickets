"""my_website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url, include
from django.contrib import admin

from rest_framework import schemas
from rest_framework_swagger.views import get_swagger_view

from django.conf import settings
from django.conf.urls.static import static

from main import views as main_views

schema_view = schemas.get_schema_view()
swagger_view = get_swagger_view(title='my_website')

urlpatterns = [
    url(r'^$', main_views.home, name='main-home'),
    url(r'^grappelli/', include('grappelli.urls')),  # grappelli URLS
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include('api.urls')),
    url(r'^users/', include('users.urls')),
    url(r'^schema/', schema_view),
    url(r'^swagger/', swagger_view),
    url(r'^about/', main_views.about, name='main-about'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
