from django.shortcuts import render
from django.http import JsonResponse
import requests
from django.views.generic import View
from drchrono.get_drchrono_data import data_from_url
from datetime import datetime
from drchrono.post_drchrono_data import patch_appointment,patch_patient
from drchrono.utils import new_appointment
# Create your views here.



def home(request):
    return render(request,'kiosk.html')

class PatientView(View):
    '''
    MAIN FUNCTION TO GET AND PATCH PATIENT DATA TO AND FROM DRCHRONO API
    '''
    def get(self, request):

        if (request.GET.has_key("f_name") and request.GET.has_key("l_name") and request.GET.has_key("dob")):
            filter = {
                    'first_name' : request.GET.get('f_name'),
                    'last_name' : request.GET.get('l_name'),
                    'date_of_birth' : request.GET.get('dob'),
            }
            patient = data_from_url(request,'https://drchrono.com/api/patients',filter)[0]
            return JsonResponse(patient)
        else:
            return JsonResponse({"status": "false"}, status=500)

    def post(self, request):

        if (request.POST.has_key("patient_id")):
            status_code = patch_patient(request)
            return JsonResponse({"response": status_code})
        else:
            return JsonResponse({"status": "false"}, status=500)


class AppointmentView(View):
    '''
    MAIN FUNCTION TO GET AND PATCH APPOINTMENT DATA TO AND FROM DRCHRONO API
    '''
    def get(self, request):
        if (request.GET.has_key("p_id")):
            now = datetime.now()
            date = now.strftime('%Y-%m-%d')
            test = data_from_url(request,'https://drchrono.com/api/appointments',{"date": date,"patient":request.GET.get('p_id')})[0]
            return JsonResponse(test)
        else:
            return JsonResponse({"status": "false"}, status=500)

    def post(self, request):
        if (request.POST.has_key('appointment_id') ):
            new_appointment(request.POST['appointment_id'],request.POST['first_name'],request.POST['last_name'])
            status_code = patch_appointment(request)
            return JsonResponse({"response": status_code})
        else:
            return JsonResponse({"status": "false"}, status=500)
