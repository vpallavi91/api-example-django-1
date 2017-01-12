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


def get_params(request, idk):
    p = {}
    keys = request.POST.keys()
    for k in keys:
        if k != idk:
            p[k] = request.POST[k]
    return p

def patch_appointment(request):

    access_token = request.session['access_token']
    appointment_id = request.POST['appointment_id']
    params = get_params(request, 'appointment_id')
    appointment_url = 'https://drchrono.com/api/appointments/' + str(appointment_id)
    status_code = patch_to_url(appointment_url, access_token, params)
    return status_code
