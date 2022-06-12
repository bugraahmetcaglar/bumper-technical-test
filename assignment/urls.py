from django.conf.urls import url
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import routers, permissions

router = routers.DefaultRouter()

schema_view = get_schema_view(
    openapi.Info(
        title="Demo - API Docs",
        default_version='v1',
        description="Demo API Documentation",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="info@demo.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('v1/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('v1/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc-ui'),
    url(r'^', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    # path('admin/', admin.site.urls),

    # User
    path('api/v1/', include("user.urls")),
    path('api/v1/', include("guestbook.urls")),
]
