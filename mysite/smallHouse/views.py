from django.shortcuts import render
from smallHouse.models import SmallHouseRealestate, SmallHouseRealnews
from smallHouse.models import TransInfo
from django.db.models import Avg

from django.http import JsonResponse
from django.http import HttpResponse

import json
import re
from django.core.serializers.json import DjangoJSONEncoder

def mainView(request):
    print("main###############################################")
    news = SmallHouseRealnews.objects.all()
    print( news.query )

    return render(request, 'main/main.html',{'news': news})

def getAddress(request):
    print("getAddr##################################################")
    if request.method == "GET":

        word= request.GET['word']
        buy_type = request.GET['buy_type']
        addrList = []
        addrList = SmallHouseRealestate.objects.raw(
            '''
            select distinct on(name) name onlyOne, id, trunc(AVG(price::numeric)) as price, location, loc_num
            from        small_house_realestate
            where       location = %s
            and         buy_type = %s
            group by    name, location, loc_num, id
            ;
            ''',
            [word,buy_type]
        )
        print(type(addrList))
        print(addrList)
        dataList = []
        result = {}
        for li in addrList:
            temp = {}
            temp['name'] = li.name.strip()
            temp['price_avg'] = str(li.price)[:-4] + "." + str(li.price)[-4:-3]
            temp['location'] = li.location
            temp['loc_num'] = li.loc_num
            temp['area_average'] = int(float(li.area_average)/3.3057)
            temp['loc_num'] = li.loc_num
            dataList.append(temp)
        result['result'] = dataList
        print(result)
    return HttpResponse(json.dumps(result, cls=DjangoJSONEncoder), content_type="application/json")

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

def getDetail(request):
    print("getDetail#################################################################################")

    if request.method == "GET":

        bldgName = request.GET['paramMap[bldg_name]'].strip()
        addrDetail = request.GET['paramMap[addr_detail]'].strip()
        buyType = request.GET['paramMap[buy_type]'].strip()
        print(buyType, "####################################################################3333")        

        detailInfo = SmallHouseRealestate.objects.filter(name=bldgName, buy_type=buyType)
        
        result = {}
        dataList = []
        priceTemp = {}
        priceTemp['floorTotalPrice'] = float(0)
        index = 1
        for li in detailInfo:
            temp = {}
            eachPrice = li.price
            temp['name'] = li.name.strip()
            if buyType == '01':
                temp['price'] = str(li.price)[:-4] + "." + str(li.price)[-4:-3]
            else:
                temp['price'] = str(li.price_deposit) + "/" + str(li.price_monthly)
            temp['fnd_year'] = li.fnd_year
            temp['sold_date'] = li.sold_date
            temp['location'] = li.location
            temp['loc_num'] = li.loc_num
            temp['floor'] = li.floor
            temp['area_average'] = int(float(li.area_average)/3.3057)
            temp['buy_type'] = li.buy_type
            temp['bldg_type'] = li.bldg_type
            priceTemp['floorTotalPrice'] += float(eachPrice)
            dataList.append(temp)
            index += 1

        result['result'] = dataList
        result['addrDetail'] = addrDetail
        avg = priceTemp['floorTotalPrice']/index
        result['avgPrice'] = str(int(avg))[:-4] + "." + str(int(avg))[-4:-3]
        
        
    return HttpResponse(json.dumps(result), content_type="application/json")


