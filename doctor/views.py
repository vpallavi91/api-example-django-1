from django.shortcuts import render,render_to_response
from django.http import JsonResponse
import requests
from django.views.generic import View
from drchrono.utils import data_from_url, patch_appointment
from datetime import datetime

# Create your views here.
def home(request):
    return render_to_response('doctor.html',{'username':request.session['un']})


class AppointmentView(View):

    def get(self, request):
        print("success")
        now = datetime.now()
        date = now.strftime('%Y-%m-%d')
        test = data_from_url(request,'https://drchrono.com/api/appointments',{"date": date})
        print(test)
        return JsonResponse({"response":test})


    def post(self, request):
        if (request.POST.has_key('appointment_id') ):
            print("inside view")
            status_code = patch_appointment(request)
            #Appointment.objects.create_appointment(request)
            return JsonResponse({"response": status_code})
        else:
            return JsonResponse({"status": "false"}, status=500)
