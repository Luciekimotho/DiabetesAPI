"""diabetesproj URL Configuration

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
from django.conf.urls import include, url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from diabetes import views

urlpatterns = [
url(r'^diabetes/', include('diabetes.urls')),
url(r'^admin/', admin.site.urls),

url(r'^users/', views.ProfileList.as_view()),
url(r'^user/(?P<pk>[0-9]+)/$', views.ProfileDetail.as_view()),

url(r'^readings/', views.ReadingsList.as_view()),
url(r'^reading/(?P<pk>[0-9]+)/$', views.ReadingDetail.as_view()),

url(r'^userreadings/', views.UserReadingsList.as_view()),
url(r'^userreading/(?P<pk>[0-9]+)/$', views.UserReading.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
