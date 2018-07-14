from django.shortcuts import render
from smallHouse.models import SmallHouseRealestate, SmallHouseRealnews
from smallHouse.models import TransInfo
from django.http import JsonResponse
from django.http import HttpResponse
import json

def mainView(request):
    print("main###############################################")
    news = SmallHouseRealnews.objects.all()
    print( news.query )

    return render(request, 'main/main.html',{'news': news})

def getAddress(request):
    print("getAddr##################################################")
    if request.method == "GET":
            
        word= request.GET['word']
        addrList = SmallHouseRealestate.objects.filter(location=word)
        print(addrList.query)
        dataList = []
        result = {}
        for li in addrList:
            temp = {}
            temp['name'] = li.name
            temp['price'] = li.price
            temp['price_deposit'] = li.price
            temp['price_monthly'] = li.price
            temp['fnd_year'] = li.fnd_year
            temp['sold_date'] = li.sold_date
            temp['location'] = li.location
            temp['loc_num'] = li.loc_num
            temp['loc_cd'] = li.loc_cd
            temp['floor'] = li.floor
            temp['area_average'] = li.floor
            temp['buy_type'] = li.floor
            temp['bldg_type'] = li.floor
            dataList.append(temp)
        result['result'] = dataList
    return HttpResponse(json.dumps(result), content_type="application/json")

def getBusStop(request):
    print("getBusStop#################################################################################")

    if request.method == "GET":
        
        lat_start = request.GET['lat_start']
        lat_end = request.GET['lat_end']
        lng_start = request.GET['lng_start']
        lng_end = request.GET['lng_end']
        busInfoList = TransInfo.objects.filter( gpslat__range=(lat_start, lat_end) )
        
        dataList = []
        result = {}
        for li in busInfoList:
            if li.gpslng >= lng_start and li.gpslng <= lng_end:
                temp = {}
                temp['name'] = li.name
                temp['gpslat'] = li.gpslat
                temp['gpslng'] = li.gpslng
                dataList.append(temp)
        result['result'] = dataList
        print(result)
    return HttpResponse(json.dumps(result), content_type="application/json")
