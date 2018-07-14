from django.shortcuts import render
from directory_tree import Root
  
def home(request):     
    return render(request, 'base/home.html', {})

def messenger(request):
    return render(request, 'base/messenger.html', {})
    
def issue_bot(request):
    return render(request, 'base/issue_bot.html', {})
    
def vr_game(request):
    return render(request, 'base/vr_game.html', {})
    
def vr_tracking(request):
    return render(request, 'base/vr_tracking.html', {})

def django_fs(request):
    root = Root()
    root.populate("fs_demo")
    return render(request, 'base/django_fs.html', {'root':root})