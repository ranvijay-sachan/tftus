from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions

from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
    openapi.Info(
        title="tftus API",
        default_version='v1.0',
        description=""" description""",
        terms_of_service="http://127.0.0.1:8000/",
        contact=openapi.Contact(email="sachan.ranvijay@gmail.com"),
        license=openapi.License(name="tftus License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/v1/', include(('cms.urls', 'cms'), namespace='cms')),
]
