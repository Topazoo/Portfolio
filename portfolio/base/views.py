from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponse
from directory_tree import Root
import requests
import json

def send_message(request):
    if request.method == 'POST':
        text = request.POST['message']
        to_number = request.POST['to_number']
        from_number = request.POST['from_number']
        carrier = request.POST['carrier']

        client = requests.session()
        url = 'http://52.25.144.62/'

        # Retrieve the CSRF token first
        client.get(url)  # sets cookie
        if 'csrftoken' in client.cookies:
            # Django 1.6 and up
            csrftoken = client.cookies['csrftoken']
        else:
            # older versions
            csrftoken = client.cookies['csrf']

        data = dict(message=text,to_number=to_number, from_number=from_number, carrier=carrier, csrfmiddlewaretoken=csrftoken)
        r = client.post(url, data=data, headers=dict(Referer=url))
        
        return HttpResponse(json.dumps({'code': 'success'}), content_type="application/json")
    return HttpResponse(json.dumps({'code': 'fail'}), content_type="application/json")

def home(request):     
    return render(request, 'base/home.html', {})

def messenger(request):
    #send_message()
    return render(request, 'base/messenger.html', {})
    
def issue_bot(request):
    return render(request, 'base/issue_bot.html', {})
    
def vr_game(request):
    return render(request, 'base/vr_game.html', {})
    
def vr_tracking(request):
    return render(request, 'base/vr_tracking.html', {})

def django_fs(request):
    direc = "fs_demo"
    if request.method == 'POST':
        direc = request.POST['dir'][:-1:]
    root = Root()
    root.populate(direc)
    return render(request, 'base/django_fs.html', {'root':root}, context_instance=RequestContext(request))