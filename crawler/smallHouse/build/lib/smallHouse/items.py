# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field

class RealEstate(scrapy.Item):
    es_name = scrapy.Field()
    price = scrapy.Field()
    fnd_year = scrapy.Field()
    sold_date = scrapy.Field()
    location = scrapy.Field()
    loc_num = scrapy.Field()
    loc_cd = scrapy.Field()
    floor = scrapy.Field()
    last_updated = scrapy.Field(serializer=str)

class EstateNews(scrapy.Item):
    title = scrapy.Field()
    newspaper = scrapy.Field()
    url = scrapy.Field()
    # up_date = scrapy.Field()

class LocationCode(scrapy.Item):
    loc_code = scrapy.Field()
    location = scrapy.Field()
