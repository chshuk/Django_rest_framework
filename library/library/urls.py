"""library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

from applic.views import AuthorViewSet, BiographyViewSet, BookViewSet, MyAPIView

router = DefaultRouter()
router.register('authors', AuthorViewSet)
router.register('books', BookViewSet)
router.register('biographies', BiographyViewSet)

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('api/', include(router.urls)),
    # path('api-token-auth/', views.obtain_auth_token),
    # re_path(r'^myapi/(?P<version>\d)/authors/$', MyAPIView.as_view({'get': 'list'}))
    # path('api/1/authors', include('applic.urls', namespace='1')),
    # path('api/2/authors', include('applic.urls', namespace='2'))
    path('api/authors', MyAPIView.as_view())
]
