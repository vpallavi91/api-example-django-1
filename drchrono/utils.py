import requests
from models import Doctor,Appointment
from get_drchrono_data import data_from_url
from datetime import datetime

def check_if_registered_doc(doc_id):
    obj = Doctor.objects.filter(doctor_id = doc_id)
    return obj.exists()

def register_doc(request,doc_id):
    filter = {
                'id': doc_id
    }
    data = data_from_url(request,'https://drchrono.com/api/doctors',filter)[0]
    doc = Doctor()
    doc.first_name = data['first_name']
    doc.last_name  = data['last_name']
    doc.doctor_id = doc_id
    doc.save()

def login_as_doc(request,doc_id):
    check = check_if_registered_doc(doc_id)
    if check == True:
        return True
    else:
        register_doc(request, doc_id)

def new_appointment(app_id):
    appointment = Appointments()
    now = datetime.now().time()
    appointment.app_id = app_id
    appointment.time_of_arrival = now
    appointment.save()
