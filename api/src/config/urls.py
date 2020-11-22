from django.contrib import admin
from django.urls import include, path, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from djoser import views as djoser_views
from django.conf import settings

schema_view = get_schema_view(
    openapi.Info(
        title="SP TEST API",
        default_version="v1",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=False,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path(f"api/{settings.USER_TYPE}/endpoints/", include("request.urls")),
    re_path(
        r"^api/" + settings.USER_TYPE + r"/swagger(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    path(
        f"api/{settings.USER_TYPE}/swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path(f"api/{settings.USER_TYPE}/admin/", admin.site.urls),
    path(
        f"api/{settings.USER_TYPE}/endpoints/user/login",
        djoser_views.TokenCreateView.as_view(),
        name="login",
    ),
]
