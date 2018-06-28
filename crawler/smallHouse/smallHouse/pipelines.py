from scrapy.exceptions import DropItem
from smallHouse.settings import SPIDER_PSQL_DB
from smallHouse.items import RealEstate
from smallHouse.items import EstateNews
import psycopg2

class EstateDealPipeline(object):

    def open_spider(self, spider):
        self.connection = psycopg2.connect("host='%s' dbname='%s' user='%s' password='%s' port='%s'" % (SPIDER_PSQL_DB['host'], SPIDER_PSQL_DB['dbname'], SPIDER_PSQL_DB['user'], SPIDER_PSQL_DB['password'], SPIDER_PSQL_DB['port']))
        self.cur = self.connection.cursor()

    def close_spider(self, spider):
        self.cur.close()
        self.connection.close()

    def process_item(self, item, spider):
        try:
            self.cur.execute("INSERT INTO small_house_realestate(name,price,fnd_year,sold_date,location,loc_num,loc_cd,floor) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)",(item['name'],item['price'],item['fnd_year'],item['sold_date'],item['location'],item['loc_num'],item['loc_cd'],item['floor']))
            print("excute################################################################################excute################################################################################")
            self.connection.commit()
        except psycopg2.InternalError as e:
            print(e)
            self.connection.rollback()
        return item


class EstateNewsPipeline(object):

    def open_spider(self, spider):
        self.connection = psycopg2.connect("host='%s' dbname='%s' user='%s' password='%s'" % (SPIDER_PSQL_DB['host'], SPIDER_PSQL_DB['dbname'], SPIDER_PSQL_DB['user'], SPIDER_PSQL_DB['password']))
        self.cur = self.connection.cursor()

    def close_spider(self, spider):
        self.cur.close()
        self.connection.close()

    def process_item(self, item, spider):
        try:
            self.cur.execute("INSERT INTO small_house_realNews(title,newspaper,url) VALUES(%s,%s,%s)",(item['title'],item['newspaper'],item['url']))
            print("excute################################################################################excute################################################################################")
            self.connection.commit()
        except psycopg2.InternalError as e:
            print(e)
            self.connection.rollback()
        return item

