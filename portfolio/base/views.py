from directory_tree import Root
from Bot import Bot
from django.shortcuts import render
from django.http import HttpResponse
import requests
import json
import os
import sys

# ------------------- Helper Functions ----------------------
def read_ini():
    ''' Reads the configuration file '''

    ini_dict = {}

    # Parse config.ini and record values
    if os.path.isfile('auth.ini'):
        with open('auth.ini') as config:
            for line in config:
                index = line.find("=")

                if index == -1:
                    print "auth.ini error - Invalid Syntax"
                    sys.exit(1)

                ini_dict[line[:index]] = line[index+1:].strip()

            config.close()

        # Check errors
        if "auth_key" not in ini_dict.keys():
            print "auth.ini error - No key Specified"
            sys.exit(1)

    else:
        print "auth.ini error - File Not Found"
        sys.exit(1)

    return ini_dict


def send_message(request, needs_auth_code=False):
    ''' Send a message request to the smartwatch messaging server '''

    # If form submitted, parse the submitted data
    if request.method == 'POST':
        text = request.POST['message']
        to_number = request.POST['to_number']
        from_number = request.POST['from_number']
        carrier = request.POST['carrier']
   
        if needs_auth_code == True:
            ini = read_ini()
            auth_code = request.POST['auth_key']
            if ini['auth_key'] != auth_code:
                return HttpResponse(json.dumps({'code': 'auth_key_invalid'}), content_type="application/json")

        client = requests.session()
        # Set the URL to the messaging server
        url = 'http://52.25.144.62/'

        # Retrieve the CSRF token 
        client.get(url)  
        if 'csrftoken' in client.cookies:
            csrftoken = client.cookies['csrftoken']
        else:
            csrftoken = client.cookies['csrf']

        # Package data
        data = dict(message=text,to_number=to_number, from_number=from_number, carrier=carrier, csrfmiddlewaretoken=csrftoken)
        
        # Send data in a POST request
        client.post(url, data=data, headers=dict(Referer=url))
        
        # Return response to AJAX request
        return HttpResponse(json.dumps({'code': 'success'}), content_type="application/json")

    # Return response to AJAX request
    return HttpResponse(json.dumps({'code': 'fail'}), content_type="application/json")

def get_top_user(subreddit):
    ''' Get the top 3 users for a subreddit '''

    # Prefix if needed
    if "r/" not in subreddit:
        subreddit = prefix_subreddit(subreddit)

    # Instantiate a Bot
    bot = Bot()
    
    # Set the subreddit and get the top 3 users
    bot.subreddits = subreddit
    bot.get_subreddits()
    bot.get_users(user_count=3, comment_count=0)

    return bot.subreddits[0].top_posters

def prefix_subreddit(subreddit):
    ''' Add '/r' to a subreddit name '''
    return "r/" + subreddit
# -----------------------------------------------------------

# ----------------------- Home Pages ------------------------
def home_site(request):     
    ''' Home Code Page '''
    return render(request, 'home/home_site.html', {})
def home_resume(request):     
    ''' Home Resume Page '''
    return render(request, 'home/home_resume.html', {})
def home(request):     
    ''' Home Page '''
    return render(request, 'home/home.html', {})
# -----------------------------------------------------------

# ---------------------- Messenger Pages --------------------
def messenger_client(request):
    ''' Messenger Client Page '''
    return render(request, 'messenger/messenger_client.html', {})
def messenger_server(request):
    ''' Messenger Server Page '''
    return render(request, 'messenger/messenger_server.html', {})
def messenger(request):
    ''' Messenger Home Page '''
    return render(request, 'messenger/messenger.html', {})
# -----------------------------------------------------------

# ------------------------- Bot Pages -----------------------
def issue_bot_bot(request):    
    ''' Bot Code Page '''
    return render(request, 'issue_bot/issue_bot_bot.html', {})
def issue_bot_analyzer(request):    
    ''' Bot Analyzer Page '''
    return render(request, 'issue_bot/issue_bot_analyzer.html', {})
def issue_bot_paper(request):    
    ''' Bot Research Paper Page '''
    return render(request, 'issue_bot/issue_bot_paper.html', {})
def issue_bot(request):
    ''' Bot Home Page '''
    
    top_users = None
    subreddit = "None"

    if request.method == 'POST':
        # If form submitted, get top users for submitted subreddit
        subreddit = request.POST['subreddit']
        top_users = get_top_user(subreddit)
    
    return render(request, 'issue_bot/issue_bot.html', {'users': top_users, 'subreddit':subreddit})
# -----------------------------------------------------------

# ----------------------- Game Pages ------------------------
def vr_game_code(request):
    ''' VR Game Code Page '''
    return render(request, 'vr_game/vr_game_code.html', {})
def vr_game_code_holding(request):
    ''' VR Game Code Page '''
    return render(request, 'vr_game/vr_game_code_holding.html', {})
def vr_game_code_shooting(request):
    ''' VR Game Code Page '''
    return render(request, 'vr_game/vr_game_code_shooting.html', {})
def vr_game_scripts(request):
    ''' VR Game Scripts Page '''
    return render(request, 'vr_game/vr_game_scripts.html', {})
def vr_game(request):
    ''' VR Game Home Page '''
    return render(request, 'vr_game/vr_game.html', {})
# -----------------------------------------------------------

# --------------------- Tracking Pages ----------------------
def vr_tracking_code(request):
    ''' Tracking Code Page'''
    return render(request, 'vr_tracking/vr_tracking_code.html', {})
def vr_tracking_gui(request):
    ''' Tracking GUI Page'''
    return render(request, 'vr_tracking/vr_tracking_gui.html', {})
def vr_tracking(request):
    ''' Tracking Home Page'''
    return render(request, 'vr_tracking/vr_tracking.html', {})
# -----------------------------------------------------------

# -------------------- Filesystem Pages ---------------------
def django_fs_code(request):
    ''' Filesystem Code Page'''
    return render(request, 'django_fs/django_fs_code.html', {})
def django_fs_templates(request):
    ''' Filesystem Template Page'''
    return render(request, 'django_fs/django_fs_templates.html', {})
def django_fs(request):
    ''' Filesystem Home Page'''
   
   # Set default directory
    direc = "fs_demo"
   
    if request.method == 'POST':
        # If form submitted, dynamically map submitted directory
        direc = request.POST['dir'][:-1:]
   
    root = Root()
    root.populate(direc)
   
    return render(request, 'django_fs/django_fs.html', {'root':root})
# -----------------------------------------------------------
