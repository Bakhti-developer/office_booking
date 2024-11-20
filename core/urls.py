from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import OfficeViewSet, RoomViewSet, BookingViewSet

router = DefaultRouter()
router.register(r'offices', OfficeViewSet, basename='office')
router.register(r'rooms', RoomViewSet, basename='room')
router.register(r'bookings', BookingViewSet, basename='booking')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny

schema_view = get_schema_view(
    openapi.Info(
        title="Office Booking API",
        default_version='v1',
        description="API for managing offices, rooms, and bookings",
    ),
    public=True,
    permission_classes=(AllowAny,),
)

urlpatterns += [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
