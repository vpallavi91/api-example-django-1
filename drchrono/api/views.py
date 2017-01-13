from django.http import JsonResponse
from drchrono.models import Doctor,Appointment
from serializers import DoctorSerializer, AppointmentSerializer

def doctor_detail(request):
    """
    Retrieve a doctor detail.
    """
    try:
        doctor = Doctor.objects.get(doctor_id=request.session['doc_id'])
    except Doctor.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = DoctorSerializer(doctor)
        return JsonResponse(serializer.data)

def appointment_detail(request,app_id):
    """
    Retrieve an appointment detail.
    """
    try:
        appointment = Appointment.objects.get(app_id=app_id)
    except Appointment.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = AppointmentSerializer(appointment)
        return JsonResponse(serializer.data)

def appointment_list(request):
    """
    Retrieve full appointment list.
    """
    if request.method == 'GET':
        appointments = Appointment.objects.all()
        serializer = AppointmentSerializer(appointments, many=True)
        return JsonResponse(serializer.data,safe=False)
