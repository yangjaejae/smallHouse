# -*- coding: utf-8 -*-
import scrapy
import re
from smallHouse.items import RealEstate
from smallHouse.dao.getLocCode import getCodeList 

class RealestaterentSpider(scrapy.Spider):
    name = 'realestateRent'
    custom_settings = {
        'ITEM_PIPELINES': {
            'smallHouse.pipelines.EstateRentPipeline': 400
        }
    }
    allowed_domains = ['openapi.molit.go.kr:8081']
    url = 'http://openapi.molit.go.kr:8081/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcRHRent'
    paramStart = "?"
    paramKey = "serviceKey=" + "rT6uASLrRFxQ65le9RBoWhItpo0g1RAWFfhyqXDWGOMki6GAZ83wP8McTHwmX0q%2FgMoPUnhrYfBBlLL3LhwO%2Fw%3D%3D"
    paramDEAL_YMD = "&DEAL_YMD=" + "201512"

    # db에 저장된 지역코드를 가져온다.
    rows = getCodeList()
    paramLAWD_CDList = []

    fullUrlList = []
    i = 0    

    for row in rows:
        paramLAWD_CDList.append("&LAWD_CD=" + row[0])
        fullUrlList.append( url + paramStart + paramKey + paramLAWD_CDList[i] + paramDEAL_YMD )
        i += 1

    start_urls = []
    start_urls = fullUrlList

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, callback = self.parse)

    def parse(self, response):
        response.selector.remove_namespaces()
        data = response.xpath('//items')
        for li in data:
            each = li.xpath('//item').extract()
            for e in each:
                item = RealEstate()
                if re.findall(r'<연립다세대>(.*?)</연립다세대>',e):
                    item['name'] = re.findall(r'<연립다세대>(.*?)</연립다세대>',e)[0].strip()
                item['price'] = 0
                if re.findall(r'<보증금액>(.*?)</보증금액>',e):
                    item['price_deposit'] = re.findall(r'<보증금액>(.*?)</보증금액>',e)[0].strip().replace(",","")
                if re.findall(r'<월세금액>(.*?)</월세금액>',e):
                    item['price_monthly'] = re.findall(r'<월세금액>(.*?)</월세금액>',e)[0].strip().replace(",","")
                if re.findall(r'<건축년도>(.*?)</건축년도>',e):
                    item['fnd_year'] = re.findall(r'<건축년도>(.*?)</건축년도>',e)[0].strip()
                if re.findall(r'<년>(.*?)</년>',e):
                    item['sold_date'] =  year = re.findall(r'<년>(.*?)</년>',e)[0] + "." + re.findall(r'<월>(.*?)</월>',e)[0]
                if re.findall(r'<법정동>(.*?)</법정동>',e):
                    item['location'] = re.findall(r'<법정동>(.*?)</법정동>',e)[0].strip()
                if re.findall(r'<지번>(.*?)</지번>',e):
                    item['loc_num'] = re.findall(r'<지번>(.*?)</지번>',e)[0].strip()
                if re.findall(r'<지역코드>(.*?)</지역코드>',e):
                    item['loc_cd'] = re.findall(r'<지역코드>(.*?)</지역코드>',e)[0].strip()
                if re.findall(r'<층>(.*?)</층>',e):
                    item['floor'] = re.findall(r'<층>(.*?)</층>',e)[0].strip()
                if re.findall(r'<전용면적>(.*?)</전용면적>',e):
                    item['area_average'] = re.findall(r'<전용면적>(.*?)</전용면적>',e)[0].strip()
                    item['bldg_type'] = '01'
                    item['buy_type'] = '02'
                yield item
