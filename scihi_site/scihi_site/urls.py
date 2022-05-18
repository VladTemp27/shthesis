"""scihi_site URL Configuration

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

from django.contrib import admin
from django.urls import path,include
from s_portal import views
from account import views



from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.index, name="index"),
    path("about", views.about, name="about"),
    path("portal", views.portal, name="portal"),
    path("covid19response", views.c19respo, name="covid19response"),
    path("jhs",views.jhs, name="jhs"),
    path("", include('s_portal.urls')),
    path("clubs", views.clubs, name="clubs"),
    path("shs", views.shs, name="shs"),
    path("accountapp/", include('account.urls')),
    path("dashboard", views.dashboard, name="dashboard")


]
