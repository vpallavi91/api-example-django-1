from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    #url(r'^patient/', views.PatientView.as_view()),
    url(r'^appointment/', views.AppointmentView.as_view()),
    ]
