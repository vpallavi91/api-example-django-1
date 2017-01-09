from django.conf.urls import include, url
from django.views.generic import TemplateView

from django.contrib import admin

import views

urlpatterns = [
    #url(r'^$', TemplateView.as_view(template_name='index.html'), name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.login,name = 'login'),
    url(r'^patients/', include('patients.urls'),name = 'doctor'),
    url(r'^doctor/', include('doctor.urls'),name = 'doctor'),
    url(r'^logout/$', views.logout_app,name = 'logout'),
    url(r'', include('social.apps.django_app.urls', namespace='social')),
]
