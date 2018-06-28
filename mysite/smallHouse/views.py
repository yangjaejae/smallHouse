from django.shortcuts import render
from legacydb.models import SmallHouseRealestate, SmallHouseRealnews

def mainView(request):
    
    news = SmallHouseRealnews.objects.using('legacydb').all()

    return render(request, 'main/main.html',{'news': news})