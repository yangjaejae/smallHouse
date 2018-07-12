# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field

class RealEstate(scrapy.Item):
    name = scrapy.Field()
    price = scrapy.Field()
    price_deposit = scrapy.Field()
    price_monthly = scrapy.Field()
    fnd_year = scrapy.Field()
    sold_date = scrapy.Field()
    location = scrapy.Field()
    loc_num = scrapy.Field()
    loc_cd = scrapy.Field()
    floor = scrapy.Field()
    area_average = scrapy.Field()
    buy_type = scrapy.Field()
    bldg_type = scrapy.Field()
    last_updated = scrapy.Field(serializer=str)

class EstateNews(scrapy.Item):
    title = scrapy.Field()
    newspaper = scrapy.Field()
    url = scrapy.Field()
    summary = scrapy.Field()
    wr_date = scrapy.Field()
    # up_date = scrapy.Field()

class LocationCode(scrapy.Item):
    loc_code = scrapy.Field()
    location = scrapy.Field()

class Trans_info(scrapy.Item):
    num = scrapy.Field()
    name = scrapy.Field()
    gpslat = scrapy.Field()
    gpslng = scrapy.Field()
    trans_type = scrapy.Field()
