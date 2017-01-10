from django.conf.urls import include, url
from django.views.generic import TemplateView
import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    ]
