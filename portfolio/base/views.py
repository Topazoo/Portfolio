from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponse
from directory_tree import Root
from Bot import Bot
import requests
import json

def home(request):     
    return render(request, 'base/home.html', {})

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


def messenger(request):
    return render(request, 'messenger/messenger.html', {})
def messenger_client(request):
    return render(request, 'messenger/messenger_client.html', {})
def messenger_server(request):
    return render(request, 'messenger/messenger_server.html', {})
    
def prefix_subreddit(subreddit):
    return "r/" + subreddit

def get_top_user(subreddit):

    if "r/" not in subreddit:
        subreddit = prefix_subreddit(subreddit)

    bot = Bot()
    
    bot.subreddits = subreddit
    bot.get_subreddits()
    bot.get_users(3,0)

    return bot.subreddits[0].top_posters

def issue_bot(request):
   
    top_users = None
    subreddit = "None"

    if request.method == 'POST':
        subreddit = request.POST['subreddit']
        top_users = get_top_user(subreddit)
    
    return render(request, 'issue_bot/issue_bot.html', {'users': top_users, 'subreddit':subreddit})

def issue_bot_bot(request):    
    return render(request, 'issue_bot/issue_bot_bot.html', {})
def issue_bot_analyzer(request):    
    return render(request, 'issue_bot/issue_bot_analyzer.html', {})
def issue_bot_paper(request):    
    return render(request, 'issue_bot/issue_bot_paper.html', {})
    
def vr_game(request):
    return render(request, 'base/vr_game.html', {})
    
def vr_tracking(request):
    return render(request, 'base/vr_tracking.html', {})

def django_fs_code(request):
    return render(request, 'django_fs/django_fs_code.html', {})
def django_fs(request):
   
    direc = "fs_demo"
   
    if request.method == 'POST':
        direc = request.POST['dir'][:-1:]
   
    root = Root()
    root.populate(direc)
   
    return render(request, 'django_fs/django_fs.html', {'root':root}, context_instance=RequestContext(request))