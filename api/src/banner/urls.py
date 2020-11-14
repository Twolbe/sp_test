from rest_framework.routers import DefaultRouter
from banner.views import BannerViewSet

default_router = DefaultRouter()

default_router.register("banners", BannerViewSet, basename="banners")

urlpatterns = default_router.urls
