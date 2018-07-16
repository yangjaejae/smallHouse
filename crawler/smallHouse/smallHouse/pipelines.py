from scrapy.exceptions import DropItem
from smallHouse.settings import SPIDER_PSQL_DB
from smallHouse.items import RealEstate
from smallHouse.items import EstateNews
import psycopg2

class EstateDealPipeline(object):

    def open_spider(self, spider):
        self.connection = psycopg2.connect("host='%s' dbname='%s' user='%s' password='%s' port='%s'" % (SPIDER_PSQL_DB['host'], SPIDER_PSQL_DB['dbname'], SPIDER_PSQL_DB['user'], SPIDER_PSQL_DB['password'], SPIDER_PSQL_DB['port']))
        self.cur = self.connection.cursor()
        self.cur.execute(
            '''
            CREATE TABLE IF NOT EXISTS small_house_realestate(
                id SERIAL PRIMARY KEY,
                name char(100),
                price int,
                price_deposit int,
                price_monthly int,
                fnd_year varchar(20),
                sold_date varchar(20),
                location varchar(20),
                loc_num varchar(20),
                loc_cd varchar(20),
                floor int,
                area_average numeric,
                buy_type int,
                bldg_type int
            )
            '''
        )
        self.connection.commit()

    def close_spider(self, spider):
        self.cur.close()
        self.connection.close()

    def process_item(self, item, spider):
        try:
            self.cur.execute("INSERT INTO small_house_realestate(name,price,price_deposit,price_monthly,fnd_year,sold_date,location,loc_num,loc_cd,floor,area_average,buy_type,bldg_type) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(item['name'],item['price'],item['price_deposit'],item['price_monthly'],item['fnd_year'],item['sold_date'],item['location'],item['loc_num'],item['loc_cd'],item['floor'],item['area_average'],item['buy_type'],item['bldg_type']))
            print("excute################################################################################excute################################################################################")
            self.connection.commit()
        except psycopg2.InternalError as e:
            print(e)
            self.connection.rollback()
        return item


class EstateRentPipeline(object):
    
    def open_spider(self, spider):
        self.connection = psycopg2.connect("host='%s' dbname='%s' user='%s' password='%s' port='%s'" % (SPIDER_PSQL_DB['host'], SPIDER_PSQL_DB['dbname'], SPIDER_PSQL_DB['user'], SPIDER_PSQL_DB['password'], SPIDER_PSQL_DB['port']))
        self.cur = self.connection.cursor()
        self.cur.execute(
            '''
            CREATE TABLE IF NOT EXISTS small_house_realestate(
                id SERIAL PRIMARY KEY,
                name char(100),
                price char(20),
                price_deposit char(20),
                price_monthly char(20),
                fnd_year char(20),
                sold_date char(20),
                location char(20),
                loc_num char(20),
                loc_cd char(20),
                floor char(20),
                area_average char(20),
                buy_type char(20),
                bldg_type char(20)
            )
            '''
        )
        self.connection.commit()

    def close_spider(self, spider):
        self.cur.close()
        self.connection.close()

    def process_item(self, item, spider):
        try:
            self.cur.execute("INSERT INTO small_house_realestate(name,price,price_deposit,price_monthly,fnd_year,sold_date,location,loc_num,loc_cd,floor,area_average,buy_type,bldg_type) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(item['name'],item['price'],item['price_deposit'],item['price_monthly'],item['fnd_year'],item['sold_date'],item['location'],item['loc_num'],item['loc_cd'],item['floor'],item['area_average'],item['buy_type'],item['bldg_type']))
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
                url char(100),
                summary text,
                wr_date char(20)
            )
            '''
        )
        self.connection.commit()

    def close_spider(self, spider):
        self.cur.close()
        self.connection.close()

    def process_item(self, item, spider):
        try:
            self.cur.execute("INSERT INTO small_house_realNews(title,newspaper,url,summary,wr_date) VALUES(%s,%s,%s,%s,%s)",(item['title'],item['newspaper'],item['url'],item['summary'],item['wr_date']))
            print("excute################################################################################excute################################################################################")
            self.connection.commit()
        except psycopg2.InternalError as e:
            print(e)
            self.connection.rollback()
        return item


class TransLocationPipeline(object):
    
    def open_spider(self, spider):
        self.connection = psycopg2.connect("host='%s' dbname='%s' user='%s' password='%s' port='%s'" % (SPIDER_PSQL_DB['host'], SPIDER_PSQL_DB['dbname'], SPIDER_PSQL_DB['user'], SPIDER_PSQL_DB['password'], SPIDER_PSQL_DB['port']))
        self.cur = self.connection.cursor()
        self.cur.execute(
            '''
            CREATE TABLE IF NOT EXISTS trans_info(
                id SERIAL PRIMARY KEY,
                num int primary key,
                name varchar(20),
                gpslat varchar(20),
                gpslng varchar(20),
                trans_type integer
            )
            '''
        )
        self.connection.commit()

    def close_spider(self, spider):
        self.cur.close()
        self.connection.close()

    def process_item(self, item, spider):
        try:
            self.cur.execute("INSERT INTO trans_info(num,name,gpslat,gpslng,trans_type) VALUES(%s,%s,%s,%s,%s)",(item['num'],item['name'],item['gpslat'],item['gpslng'],item['trans_type']))
            print("excute################################################################################excute################################################################################")
            self.connection.commit()
        except psycopg2.InternalError as e:
            print(e)
            self.connection.rollback()
        return item

