# -*- coding: utf-8 -*-
import scrapy
import re
from smallHouse.items import Trans_info
import openpyxl
import xlrd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class TranslocationSpider(scrapy.Spider):
    name = 'transLocation'
    custom_settings = {
        'ITEM_PIPELINES': {
            'smallHouse.pipelines.TransLocationPipeline': 500
        }
    }
    start_urls = [ 
        'http://data.seoul.go.kr/dataList/datasetView.do?infId=OA-15067&srvType=F&serviceKind=1&currentPageNo=1'
    ]

    def __init__(self):
        download_dir = '/home/yangjaeho/dev/pythonPrj/smallPrj/crawler/smallHouse/smallHouse/files'
        options = webdriver.ChromeOptions()
        options.add_experimental_option("prefs", {
            "download.default_directory": download_dir,
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "safebrowsing.enabled": True
        })
        self.driver = webdriver.Chrome('/home/yangjaeho/dev/pythonPrj/smallPrj/chromedriver', chrome_options=options)
    
    def parse(self,response):
        self.driver.implicitly_wait(3)
        self.driver.get(response.url)
        self.driver.find_element_by_css_selector("#dataDiv > div > table > tbody > tr > td:nth-child(6) > a").click()

        wb = xlrd.open_workbook('/home/yangjaeho/dev/pythonPrj/smallPrj/crawler/smallHouse/smallHouse/files/서울시 버스정류소 위치 데이터(20180502).xls')
        ws = wb.sheet_by_index(0)
        ncol = ws.ncols
        nlow = ws.nrows
        item = Trans_info()
        i = 0
        while i < nlow:
            print(ws.row_values(i))
            li = ws.row_values(i)
            item['num'] = li[0]
            item['name'] = li[1]
            item['gpslat'] = li[2]
            item['gpslng'] = li[3]
            item['trans_type'] = '01'
            yield item
            # print(item)
            i += 1