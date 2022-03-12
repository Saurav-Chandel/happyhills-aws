"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path,include,re_path
# from user.models import *
from django.conf import settings
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from django.conf.urls.static import static
from app.views import home
from django.views.static import serve
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static

schema_view = get_schema_view(
    openapi.Info(
        title="explore API",
        description="API documentation for Medical-center",
        default_version="v1",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("", home),
    path('admin/', admin.site.urls),
    path("users/",include("exploreapp.urls", namespace="user")),
    path("custom_trip/",include("custom_trip.urls", namespace="custom_trip")),
    path("Upcoming_Treks/",include("upcoming_treks.urls", namespace="upcoming_trips")),
    path("package/",include("package.urls", namespace="package")),
    path("review/",include("review.urls", namespace="review")),
    # path("reviews/",include("review.urls", namespace="review")),
    # path("stripe/",include("payments.urls", namespace="payment")),
    # path("stripe/", include("djstripe.urls", namespace="djstripe")),

    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path(
        "redoc/",
        schema_view.with_ui("redoc", cache_timeout=0),
        name="schema-redoc",
    ),
    re_path(r'^media_root/(?P<path>.*)$' ,serve,{'document_root':settings.MEDIA_ROOT}),
]


# if settings.DEBUG:
urlpatterns += [] + static(
    settings.STATIC_URL, document_root=settings.STATIC_ROOT
)
urlpatterns += [] + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)

