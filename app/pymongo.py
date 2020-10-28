# installed
from pymongo import MongoClient


class PyMongoClient(object):
    def __init__(self, host: str, username: str, password: str, ssl: bool = True):
        _host = "mongodb+srv://{0}:{1}@{2}/{0}".format(
            username, password, host
        )

        self.client = MongoClient(_host, authSource="admin", ssl=ssl)
