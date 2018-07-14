# -*- coding: utf-8 -*-
import scrapy
import re
import os
from smallHouse.items import Trans_info
import openpyxl
import xlrd
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.options import Options
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
        osPath = os.getcwd()
        driverPath = osPath + '/smallHouse/driver/chromedriver'
        self.downloadPath = osPath + '/smallHouse/files/'

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("prefs", {
            "download.default_directory": self.downloadPath,
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "safebrowsing.enabled": True
        })
        # options.set_preference("browser.download.folderList", 2)
        # options.set_preference("browser.download.manager.showWhenStarting", False)
        # options.set_preference("browser.download.manager.showAlertOnComplete", False)
        # options.set_preference("browser.download.dir", downloadPath)
        # options.set_preference("browser.helperApps.neverAsk.saveToDisk", "")
        self.driver = webdriver.Chrome(executable_path =driverPath, chrome_options=chrome_options)
    
    def parse(self,response):
        
        self.driver.implicitly_wait(3)
        self.driver.get(response.url)
        self.driver.find_element_by_css_selector("#dataDiv > div > table > tbody > tr > td:nth-child(6) > a").click()
        inputFilePath = self.downloadPath + '서울시 버스정류소 위치 데이터(20180502).xls'
        wb = xlrd.open_workbook(inputFilePath)
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

# /home/yangjaeho/dev/pythonPrj/smallPrj/crawler/smallHouse/smallHouse/files/서울시 버스정류소 위치 데이터(20180502).xls
# /home/yangjaeho/dev/pythonPrj/smallPrj/crawler/smallHouse/smallHouse/files/서울시 버스정류소 위치 데이터(20180502).xls'