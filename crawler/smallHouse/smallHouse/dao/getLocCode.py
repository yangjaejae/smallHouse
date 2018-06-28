import psycopg2
from smallHouse.items import LocationCode
from smallHouse.settings import SPIDER_PSQL_DB

def getCodeList():
    try:
        connection = psycopg2.connect("host='%s' dbname='%s' user='%s' password='%s' port='%s'" % (SPIDER_PSQL_DB['host'], SPIDER_PSQL_DB['dbname'], SPIDER_PSQL_DB['user'], SPIDER_PSQL_DB['password'], SPIDER_PSQL_DB['port']))
    except psycopg2.NotSupportedError as e:
        print(e.pgerror)

    cur = connection.cursor()
    cur.execute("SELECT loc_code FROM location_code")
    rows = cur.fetchall()
    cur.close()
    connection.close()
    return rows
