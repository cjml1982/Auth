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
from authapp.views import ResponseView,AuthView,UpdateView,AdminView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^asym-auth/register/',RegisterView),
    url(r'^asym-auth/authRequest/',RequestView),
    url(r'^asym-auth/response/',ResponseView),
    url(r'^asym-auth/verify/',AuthView),
    url(r'^asym-auth/update/(?P<function>(\w+))',UpdateView),
    url(r'^asym-auth/admin/(?P<function>(\w+))',AdminView),
    #url(r'^asym-auth/update/(?P<function>(\w+))/(?P<id>(\d+))',UpdateView),
]

