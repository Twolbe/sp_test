from rest_framework.routers import DefaultRouter

from .views import RequestViewSet

default_router = DefaultRouter()

default_router.register("request", RequestViewSet, basename="request")

urlpatterns = default_router.urls