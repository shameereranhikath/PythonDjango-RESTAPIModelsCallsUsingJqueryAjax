"""website URL Configuration

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
from django.contrib import admin
from django.urls import path,include
from rest_framework.urlpatterns import format_suffix_patterns
from companies import  views
from django.contrib.staticfiles.urls import  staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',include('companies.urls')),
    path('stock/',views.StockList.as_view()),

]

urlpatterns+=staticfiles_urlpatterns()
urlpatterns=format_suffix_patterns(urlpatterns)
