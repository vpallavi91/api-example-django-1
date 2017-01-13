import requests


def patch_to_url(url, access_token, params={}):
    '''
    MAIN FUNCTION TO PATCH DATA TO DRCHRONO API
    '''
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
        if k not in idk:
            p[k] = request.POST[k]
    return p

def patch_appointment(request):
    '''
    HELPER FUNCTION TO PATCH APPOINTMENT DATA TO DRCHRONO API
    '''
    access_token = request.session['access_token']
    appointment_id = request.POST['appointment_id']
    id_keys = []
    id_keys.append('appointment_id')
    if(request.POST.has_key('first_name')):
        id_keys.append('first_name')
        id_keys.append('last_name')
    params = get_params(request, id_keys)
    appointment_url = 'https://drchrono.com/api/appointments/' + str(appointment_id)
    status_code = patch_to_url(appointment_url, access_token, params)
    return status_code


def patch_patient(request):
    '''
    HELPER FUNCTION TO PATCH PATIENT DATA TO DRCHRONO API
    '''
    access_token = request.session['access_token']
    patient_id = request.POST['patient_id']
    id_keys = []
    id_keys.append('patient_id')
    params = get_params(request, id_keys)
    patient_url = 'https://drchrono.com/api/patients/' + str(patient_id)
    status_code = patch_to_url(patient_url, access_token, params)
    return status_code
