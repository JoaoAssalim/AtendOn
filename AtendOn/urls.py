from django.contrib import admin
from django.urls import path, include, reverse_lazy, re_path
from django.views.generic import RedirectView
from django.contrib.auth.decorators import login_required
from django.views.i18n import JavaScriptCatalog

from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions


admin.site.site_header = 'Administration'

urlpatterns_panel_admin_redirect = [
    path('api/', RedirectView.as_view(url='/api/swagger/', permanent=False)),
]

urlpatterns_api = [
    path('api/authentication/', include('core.account.api.urls')),
    path('api/clients-control/', include('core.clients.api.urls')),
]

schema_view = get_schema_view(
    openapi.Info(
        title='AtendOn API',
        default_version='v1.0',
        description='',
        terms_of_service='https://www.google.com/policies/terms/',
        contact=openapi.Contact(email='joassalim@gmail.com'),
        license=openapi.License(name='BSD License'),
    ),
    patterns=urlpatterns_api,
    public=True
)

urlpatterns = [
                path('admin/', admin.site.urls), 
              ] + urlpatterns_api + [
                  re_path(r'api/swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
                    re_path(r'system-status-v0qw/', include('health_check.urls'))
                ] + \
              urlpatterns_panel_admin_redirect