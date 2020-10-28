# installed
from pymongo import MongoClient


class PyMongoClient(object):
    def __init__(self, host: str, username: str, password: str, ssl: bool = True):
        _host = "mongodb+srv://{0}:{1}@{2}/{0}".format(
            username, password, host
        )

        self.client = MongoClient(_host, authSource="admin", ssl=ssl)


class DatabaseManager(object):
    def __init__(self, client: PyMongoClient, database: str, collection: str):
        self.collection = client[database][collection]

    def insert_one(self, data: dict = {}) -> dict:
        results = self.collection.insert_one(data)
        return results

    def find_one(self, filters: dict = {}) -> dict:
        results = self.collection.find_one(filters)
        return results

    def find(self, filters: dict = {}, limit: int = 25, page: int = 1) -> list:
        skip = limit * (page - 1)
        results = self.collection.find(filters).skip(skip).limit(limit)
        return list(results)

    def update_one(self, filters: dict = {}, data: dict = {}) -> dict:
        results = self.collection.update_one(
            filters,
            {"$set": data}
        )
        return results

    def update_many(self, filters: dict = {}, data: dict = {}) -> dict:
        results = self.collection.update_many(
            filters,
            {"$set": data}
        )
        return results

    def delete_one(self, filters) -> dict:
        results = self.collection.delete_one(filters)
        return results
