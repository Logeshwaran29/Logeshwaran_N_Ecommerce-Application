from .PropertyUtil import DBPropertyUtil
import mysql.connector as sql


class DBConnUtil:
    connection = None

    @staticmethod
    def getConnection():
        try:
            db = DBPropertyUtil.getPropertyString()
            connection = sql.connect(host=db['host'], database=db['database'], user=db['user'], password=db['password'])
            return connection
        except Exception as e:
            print(e)

