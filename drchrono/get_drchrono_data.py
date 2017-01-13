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
