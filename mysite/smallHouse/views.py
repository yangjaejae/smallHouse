from django.shortcuts import render
from legacydb.models import SmallHouseRealestate, SmallHouseRealnews
from django.http import JsonResponse
from django.http import HttpResponse
import json

def mainView(request):
    print("main###############################################")
    news = SmallHouseRealnews.objects.using('legacydb').all()

    return render(request, 'main/main.html',{'news': news})

def getAddr(request):
    print("getAddr##################################################")
    if request.method == "GET":
            
        word= request.GET['word']
        addrList = SmallHouseRealestate.objects.using('legacydb').filter(location=word)
        dataList = []
        result = {}
        for li in addrList:
            temp = {}
            temp['name'] = li.name
            temp['price'] = li.price
            temp['fnd_year'] = li.fnd_year
            temp['sold_date'] = li.sold_date
            temp['location'] = li.location
            temp['loc_num'] = li.loc_num
            temp['loc_cd'] = li.loc_cd
            temp['floor'] = li.floor
            dataList.append(temp)
        result['result'] = dataList
    return HttpResponse(json.dumps(result), content_type="application/json")
