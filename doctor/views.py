from django.shortcuts import render,render_to_response
import requests


# Create your views here.
def home(request):
    return render_to_response('doctor.html',{'username':request.session['un']})
