from django.shortcuts import render
from django.http import JsonResponse
import requests
from django.views.generic import View
from drchrono.utils import data_from_url

# Create your views here.
def home(request):
    return render(request,'kiosk.html')

class PatientView(View):
    """
        Handles get and post request to our /doctor/patient endpoint.
        Also then handles GET/POST requests to drchrono's /patients/ endpoint.
    """

    def get(self, request):
        """ Query drchrono /patients endpoint and return JSON of patient info """

        if (request.GET.has_key("f_name")):
            filter = {
                    'first_name' : request.GET.get('f_name'),
                    'last_name' : request.GET.get('l_name'),
                    'date_of_birth' : request.GET.get('dob'),
            }
            patient = data_from_url(request,'https://drchrono.com/api/patients',filter)[0]
            print(patient)
            return JsonResponse(patient)
        else:
            return JsonResponse({"status": "false"}, status=500)

    # def post(self, request):
    #     """
    #         Responds to POST request to /doctor/patient endpoint by sending
    #         PATCH request to /patients/ update to update patient info.
    #     """
    #
    #     if (request.POST.has_key("patient_id")):
    #         status_code = patch_patient(request)
    #         return JsonResponse({"response": status_code})
    #     else:
    #         return JsonResponse({"status": "false"}, status=500)


class AppointmentView(View):
    """
        Handles GET and POST requests to our /doctor/appointment/ endpoint and
        responds by sending GET or PATCH request to drchrono /appointment
    """

    def get(self, request):
        """
            Send GET request to drchrono /appointments endpoint and return
            JSON of arrays of appointments filtered by name.
        """

        if (request.GET.has_key("date")):
            filter = {
                    'date' : date
            }
            appointments = data_from_url(request,'https://drchrono.com/api/appointments',filter)
            return JsonResponse({"response": appointments})
        else:
            return JsonResponse({"status": "false"}, status=500)

    # def post(self, request):
    #     """
    #         When patient checks in, we have to
    #         send PATCH request to drchrono /appointments endpoint to update
    #         its status.
    #
    #         The /appointments endpoint does not provide the time the patient
    #         checked in. So when patient checks in, we also create a new appointment
    #         in our DB so we can save the check-in time.
    #     """
    #     if (request.POST.has_key('appointment_id') and request.POST.has_key('scheduled_time')):
    #         status_code = patch_appointment(request)
    #         Appointment.objects.create_appointment(request)
    #         return JsonResponse({"response": status_code})
    #     else:
    #         return JsonResponse({"status": "false"}, status=500)
