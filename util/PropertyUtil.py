from dotenv import load_dotenv
import os


class DBPropertyUtil:
    @staticmethod
    def getPropertyString():
        load_dotenv()

        db_prop = {
            'host': os.getenv('host'),
            'database': os.getenv('database'),
            'user': os.getenv('user'),
            'password': os.getenv('password')
        }
        return db_prop

