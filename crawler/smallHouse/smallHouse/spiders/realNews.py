# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from smallHouse.items import EstateNews
import re
# from scrapy.crawler import CrawlerProcess


class RealnewsSpider(scrapy.Spider):
    name = 'realNews'
    custom_settings = {
        'ITEM_PIPELINES': {
            'smallHouse.pipelines.EstateNewsPipeline': 200
        }
    }

    start_urls = [
        'http://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=101&sid2=260'
    ]

    def start_requests(self):
        for url in self.start_urls:
            yield Request(  url,
                            headers = {
                              'USER_AGENT' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'
                                # 'data-useragent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36'
                           },
                        callback = self.parse)
    page = 1

    def parse(self, response):

        item = EstateNews()

        for txt in response.xpath('//ul[contains(@class, "type06")]/li'):
            if txt.css('dt.photo a img::attr(alt)').extract_first() == None:

                item['title'] = "".join(txt.css('dt')[0].css('a::text').re(r'[^\t\r\n\v\f].*?[^\t\r\n\v\f]'))
                item['url'] = txt.css('dt')[0].css('a::attr(href)').extract_first()
                item['newspaper'] = txt.css('dd')[0].css('span.writing::text').extract_first()
                item['summary'] = txt.css('dd')[0].css('span.lede::text').extract_first()
                item['wr_date'] = response.css('div.pagenavi_day').css('span.viewday::text').extract_first()
            else:

                item['title'] = txt.css('dt.photo a img::attr(alt)').extract_first()
                item['url'] = txt.css('dt')[0].css('a::attr(href)').extract_first()
                item['newspaper'] = txt.css('dd')[0].css('span.writing::text').extract_first()
                item['summary'] = txt.css('dd')[0].css('span.lede::text').extract_first()
                item['wr_date'] = response.css('div.pagenavi_day').css('span.viewday::text').extract_first()
            yield item
            print(item)

        # follow
        # Request와 비교해서 follow는 url을 직접 조작하는 대신 관련된 url을 찾아서
        # 자동으로 parse를 callback
        self.page += 1
        next_page = response.xpath('//*[@id="main_content"]/div[3]/a/@href')[self.page].extract()

        if next_page is not None:
            print(self.page)
            yield response.follow(next_page, callback=self.parse)

# process = CrawlerProcess({
#     'USER_AGENT' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36'
# })

# process.crawl(RealnewsSpider)
# process.start() # the script will block here until the crawling is finished

