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
    doc.total_wait_time = 0
    doc.total_patients = 0
    doc.save()

def login_as_doc(request,doc_id):
    check = check_if_registered_doc(doc_id)
    if check == True:
        return True
    else:
        register_doc(request, doc_id)

def new_appointment(app_id,fname,lname):
    appointment = Appointment()
    now = datetime.now()
    appointment.app_id = app_id
    appointment.time_of_arrival = now
    appointment.first_name = fname
    appointment.last_name = lname
    appointment.save()

def setWaitTime(request,app_id):
    appointment = Appointment.objects.get(app_id=app_id)
    now = datetime.now()
    appointment.start_time = now
    print(str(now))
    print(appointment.time_of_arrival)
    dur = getDuration(str(now),str(appointment.time_of_arrival))
    print(dur)
    appointment.wait_time = dur
    doctor = Doctor.objects.get(doctor_id=int(request.session['doc_id']))
    doctor.total_wait_time = doctor.total_wait_time + dur
    doctor.total_patients = doctor.total_patients + 1
    doctor.save()
    appointment.save()

def getDuration(now,then):
    then_hr = int(then[11:13])
    now_hr = int(now[11:13])
    then_hr = then_hr - 8
    then_min = int(then[14:16])
    now_min = int(now[14:16])
    hr_diff = now_hr-then_hr
    print(then_hr)
    print(now_hr)
    print(hr_diff)
    if (hr_diff == 0):
        min_final = now_min - then_min
    else:
        hr_diff = hr_diff - 1
        min_final = (60 - then_min) + now_min
    return min_final
