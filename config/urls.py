from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from config import settings

# настройка работы автогенерации схем, взята из официальной документации drf-yasg
schema_view = get_schema_view(
   openapi.Info(
      title="Описание API для работы с Task",
      default_version='v1',
      description="Первая версия работы с описанием",
      terms_of_service="<https://www.google.com/policies/terms/>",
      contact=openapi.Contact(email="dev@sagirov.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes = (permissions.IsAuthenticated,),
)


urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('admin/', admin.site.urls),
    path('', include('todolist.urls', namespace='todolist')),
    path('api-auth/', include('rest_framework.urls')),
    re_path('^swagger(?P<format>\\\\.json|\\\\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('', include('users.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns