"""server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter

import server.equipments.urls
from server.accounts.views import UserViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')
urlpatterns = router.urls

urlpatterns += [
    path('admin/', admin.site.urls),
    path('equipments/', include(server.equipments.urls)),
    url(r'^docs/', include_docs_urls(title='API docs'))
]
