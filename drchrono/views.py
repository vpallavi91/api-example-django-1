# Create your views here.
import requests
import os
import time
from django.contrib.auth import logout
from django.shortcuts import render, redirect, render_to_response
from django.core.urlresolvers import reverse
import datetime
from datetime import datetime
from utils import (
    data_from_url,
    login_as_doc
    )


def login(request):
    if (request.user.is_anonymous() == True or request.user.is_authenticated() == False) :
        print "helllooooo"
        return render_to_response('index.html',{'username':''})
    else:
        instance = request.user.social_auth.get(provider='drchrono')
        user_name = str(instance)
        request.session['un'] = user_name
        request.session['access_token'] = instance.extra_data['access_token']
        data = data_from_url(request,'https://drchrono.com/api/users')
        # now = datetime.now()
        # date = now.strftime('%Y-%m-%d')
        #headers = {'Authorization': 'Bearer %s' %request.session['access_token'],}
        # test = requests.patch('https://drchrono.com/api/appointments?43986040',{"status":'Arrived'})
        # print(test)
        for da in data:
            if da['username'] == user_name:
                if da['is_doctor'] == True:
                    login_as_doc(request,da['doctor'])
        return render_to_response('index.html',{'username':user_name})

def logout_app(request):
    logout(request)
    return redirect(reverse("login"))
