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

def patch_to_url(url, access_token, params={}):

    headers = {'Authorization': 'Bearer %s' % access_token,
               'Content-type': 'application/json',}
    print("inside patch_to_url")
    response = requests.patch(url, json=params, headers=headers)

    print(response.status_code)
    return response.status_code


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

def get_params(request, idk):
    """ Given a request object that has post parameters,
        return a dictionary that maps the post keys to their values.
        Ignores the id_key. Helper for the patch_patient and
        patch_appointment functions

        Params:
            request - request object
            id_key - String. This is the key that we ignore if it
                     is a key in the post parameters
        Return:
            params - a dictionary that maps properties that will be updated
                     to their updated values. This dictionary is passed in
                     the PATCH request to the drchrono endpoint
    """
    keys = request.POST.keys()
    params = {}
    for key in keys:
        if key != idk:
            params[key] = request.POST[key]
    return params

def patch_appointment(request):
    """
        Submit a PATCH request to /appointments endpoint.

        Params:
            request - Request object with the parameters of the appointment
                      to update
        Return the status code
    """
    access_token = request.session['access_token']
    appointment_id = request.POST['appointment_id']
    params = get_params(request, 'appointment_id')
    appointment_url = 'https://drchrono.com/api/appointments/' + str(appointment_id)
    status_code = patch_to_url(appointment_url, access_token, params)
    return status_code
