"""test_project URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from landing import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^contacts$', views.contacts, name='contacts'),
    url(r'^akusticheskieudarnye$', views.akusticheskieudarnye, name='akusticheskieudarnye'),
    url(r'^ehlektronnyeudarnye$', views.ehlektronnyeudarnye, name='ehlektronnyeudarnye'),
    url(r'^instrumentysmembranoj$', views.instrumentysmembranoj, name='instrumentysmembranoj'),
    url(r'^samozvuchashchieinstrumenty$', views.samozvuchashchieinstrumenty, name='samozvuchashchieinstrumenty'),
    url(r'^zapchastiikomplektuyushchie$', views.zapchastiikomplektuyushchie, name='zapchastiikomplektuyushchie'),
    url(r'^barabannyepalochkiishchyotki$', views.barabannyepalochkiishchyotki, name='barabannyepalochkiishchyotki'),
    url(r'^checkout$', views.checkout, name='checkout'),
    url(r'^checkout_order$', views.checkout_order, name='checkout_order'),
    url(r'^landing/$', views.landing, name='landing'),
]