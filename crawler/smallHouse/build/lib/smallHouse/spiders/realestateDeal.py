# -*- coding: utf-8 -*-
import scrapy
import re
import sys
from smallHouse.items import RealEstate
from voluptuous import Schema, Match
import smallHouse.dao.getLocCode as getCode
# from smallHouse.dao import GetLocationCode
# reload(sys)
# sys.setdefaultencoding('utf-8')


class RealestatedealSpider(scrapy.Spider):
    name = 'realestateDeal'
    custom_settings = {
        'ITEM_PIPELINES': {
            'smallHouse.pipelines.EstateDealPipeline': 300
        }
    }
    allowed_domains = ['openapi.molit.go.kr:8081']
    url = "http://openapi.molit.go.kr:8081/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcRHTrade"
    paramStart = "?"
    paramKey = "serviceKey=" + "rT6uASLrRFxQ65le9RBoWhItpo0g1RAWFfhyqXDWGOMki6GAZ83wP8McTHwmX0q%2FgMoPUnhrYfBBlLL3LhwO%2Fw%3D%3D"
    paramDEAL_YMD = "&DEAL_YMD=" + "201512"

    # db에 저장된 지역코드를 가져온다.
    rows = getCode.getCodeList()
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
        schema = Schema({
            'es_name': str,
            'price': str,
            'fnd_year': str,
            'sold_date': str,
            'location': str,
            'loc_num': str,
            'loc_cd': str,
            'floor': str,
        })
        for li in data:
            each = li.xpath('//item').extract()
            for e in each:
                eachList = []
                eachData = re.sub('<[^<]+?>', ' ', e)
                eachList = eachData.split(' ')
                sold_date = eachList[10] + "." + eachList[19]
                item = RealEstate()
                schema({
                    'es_name': eachList[17],
                    'price': eachList[6],
                    'fnd_year': eachList[8],
                    'sold_date': sold_date,
                    'location': eachList[15],
                    'loc_num': eachList[25],
                    'loc_cd': eachList[27],
                    'floor': eachList[29],
                })
                item['es_name'] = eachList[17]
                item['price'] = eachList[6]
                item['fnd_year'] = eachList[8]
                item['sold_date'] = sold_date
                item['location'] = eachList[15]
                item['loc_num'] = eachList[25]
                item['loc_cd'] = eachList[27]
                item['floor'] = eachList[29]
                yield item
                print(item)