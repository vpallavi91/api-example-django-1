from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^appointment/', views.AppointmentView.as_view()),
    url(r'^report/', views.reports,name='reports'),
    ]
