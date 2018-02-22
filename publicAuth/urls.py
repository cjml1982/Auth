"""publicAuth URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from authapp.views import RegisterView 
from authapp.views import RequestView
from authapp.views import ResponseView,AuthView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^asym-auth/registration/',RegisterView),
    url(r'^asym-auth/request/',RequestView),
    url(r'^asym-auth/response/',ResponseView),
    url(r'^asym-auth/verify/(?P<function>(\w+))/(?P<id>(\d+))',AuthView),
]

