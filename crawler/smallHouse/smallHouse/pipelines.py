from scrapy.exceptions import DropItem
from smallHouse.settings import SPIDER_PSQL_DB
from smallHouse.items import RealEstate
from smallHouse.items import EstateNews
import psycopg2

class EstateDealPipeline(object):

    def open_spider(self, spider):
        self.connection = psycopg2.connect("host='%s' dbname='%s' user='%s' password='%s' port='%s'" % (SPIDER_PSQL_DB['host'], SPIDER_PSQL_DB['dbname'], SPIDER_PSQL_DB['user'], SPIDER_PSQL_DB['password'], SPIDER_PSQL_DB['port']))
        self.cur = self.connection.cursor()
        self.cur.execute('DROP TABLE small_house_realestate')
        self.connection.commit()
        self.cur.execute(
            '''
            CREATE TABLE IF NOT EXISTS small_house_realestate(
                id SERIAL PRIMARY KEY,
                name char(100),
                price char(20),
                fnd_year char(20),
                sold_date char(20),
                location char(20),
                loc_num char(20),
                loc_cd char(20),
                floor char(20)
            )
            '''
        )
        self.connection.commit()

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
        self.connection = psycopg2.connect("host='%s' dbname='%s' user='%s' password='%s' port='%s'" % (SPIDER_PSQL_DB['host'], SPIDER_PSQL_DB['dbname'], SPIDER_PSQL_DB['user'], SPIDER_PSQL_DB['password'], SPIDER_PSQL_DB['port']))
        self.cur = self.connection.cursor()
        self.cur.execute(
            '''
            CREATE TABLE IF NOT EXISTS small_house_realNews(
                id SERIAL PRIMARY KEY,
                title char(100),
                newspaper char(20),
                url char(100)
            )
            '''
        )
        self.connection.commit()

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

