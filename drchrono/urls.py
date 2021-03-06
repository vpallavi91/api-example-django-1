from django.conf.urls import include, url
from django.views.generic import TemplateView
from drchrono.api import views as api_views
from django.contrib import admin

import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.login,name = 'login'),
    url(r'^test/$', views.login,name = 'login'),
    url(r'^kiosk/', include('kiosk.urls',namespace = 'kiosk')),
    url(r'^doctor/', include('doctor.urls',namespace='doctor')),
    url(r'^detail/doctor/$', api_views.doctor_detail ),
    url(r'^detail/appointment/(?P<app_id>[0-9]+)/$', api_views.appointment_detail ),
    url(r'^list/appointment/$', api_views.appointment_list ),
    url(r'^logout/$', views.logout_app,name = 'logout'),
    url(r'', include('social.apps.django_app.urls', namespace='social')),
]
