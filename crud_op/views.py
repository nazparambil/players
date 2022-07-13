from django.shortcuts import render
from .models import players

# Create your v iews here.
def index(request):
    return render(request,"index.html")

def search(request):
    playername=request.POST['play']
    details=players.objects.filter(player_name=playername)
    return render(request,"index.html",{'dtl':details})

def displayall(request):
    allplayers=players.objects.all()
    return render(request,"index.html",{'dtl':allplayers})

def addnewplayers(request):
    name=request.POST['player_name']
    emailid=request.POST['player_email']
    p_country=request.POST['player_country']
    noofgames=request.POST['gamesplayed']
    totalscr=request.POST['totalsrc']
    newplayer=players(player_name=name,player_email=emailid,country=p_country,games=noofgames,total=totalscr)
    newplayer.save()
    return render(request,"index.html",{'add':'added'}) 

def deleteplayer(request):
    name=request.POST['player_name']
    playerfordelete=palyers.objects.filter(player_name=name)
    playerfordelete.delete()

