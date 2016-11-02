"""
@Author: Hizaoui Mohamed Abdelkader
@Email-1: hizaoui.ma@gmail.com
@Email-2: hizaoui.mohamed.abdelkader@gmail.com
@created on: '11/1/16'
"""
from bson.objectid import ObjectId
from tornado.gen import coroutine


class Database(object):
    client = None
    database = None
    collection = None

    def __init__(self, client, database, collection):
        self.client = client
        self.database = self.__get_database(database)
        self.collection = self.__get_collection(collection)

    def __get_database(self, database):
        return self.client[database]

    def __get_collection(self, collection):
        return self.database[collection]

    def __validate(self, docuement):
        docuement['_id'] = str(docuement['_id'])
        validated = {docuement['_id']: docuement}
        return validated

    @coroutine
    def create(self, data):
        yield self.collection.insert(data)
        return self.__validate(data)

    @coroutine
    def read(self, oid):
        result = {}
        if oid:
            try:
                oid = ObjectId(oid)
            except TypeError:
                return None
            document = yield self.collection.find_one({'_id': ObjectId(oid)})
            if document:
                result = self.__validate(document)
        else:
            cursor = self.collection.find({})
            while (yield cursor.fetch_next):
                document = cursor.next_object()
                result.update(self.__validate(document))
        return result

    @coroutine
    def update(self, oid, data):
        pass

    @coroutine
    def delete(self, oid):
        pass
