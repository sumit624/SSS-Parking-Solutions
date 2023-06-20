"""SSS URL Configuration

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
from SSS import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('show', views.show),
    path('', views.homepage, name='home'),
    path('book_slot', views.bookslot, name='book'),
    path('location', views.location, name='location'),
    path('register', views.register, name='register'),
    path('savedata', views.savedatas, name='savedata'),
    path('verify', views.verifydata, name='verify'),
    path('tray',views.tray, name='tray')
]
