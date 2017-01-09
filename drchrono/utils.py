import requests
from django.shortcuts import render_to_response, redirect,render
from models import Doctor



def data_from_url(request,url, filter={}):
    data = []
    headers = {'Authorization': 'Bearer %s' %request.session['access_token'],}
    while url:
        page = requests.get(url, filter, headers=headers).json()
        data.extend(page['results'])
        url = page['next']
    return data



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

def login_as_staff(doc_id):
    return check_if_registered_doc(doc_id)

def login_as_doc(request,doc_id):
    check = check_if_registered_doc(doc_id)
    if check == True:
        return True
    else:
        register_doc(request, doc_id)
