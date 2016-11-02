"""
@Author: Hizaoui Mohamed Abdelkader
@Email-1: hizaoui.ma@gmail.com
@Email-2: hizaoui.mohamed.abdelkader@gmail.com
@created on: '11/1/16'
"""
import json
from tornado.gen import coroutine
from tornado.web import RequestHandler

from api.database import Database


class MDBRequestHandler(RequestHandler):
    def initialize(self):
        self.client = self.settings['client']

    @coroutine
    def post(self, db, collection):
        database = Database(self.client, db, collection)
        params = self.get_rest_params()
        response = yield database.create(params)
        self.write_rest(response)

    @coroutine
    def get(self, db, collection, oid=None):
        database = Database(self.client, db, collection)
        response = yield database.read(oid)
        self.write_rest(response)

    @coroutine
    def patch(self, db, collection, oid=None):
        database = Database(self.client, db, collection)
        pass

    @coroutine
    def put(self, db, collection, oid=None):
        database = Database(self.client, db, collection)
        pass

    @coroutine
    def delete(self, db, collection, oid=None):
        database = Database(self.client, db, collection)
        response = yield database.delete(oid)
        self.write_rest(response)

    def get_rest_params(self):
        params = json.loads(self.request.body.decode())
        return params

    def write_rest(self, chunk):
        if not self._finished:
            if chunk:
                self.write(chunk)
            else:
                self.send_error(status_code=404)

    def write_error(self, status_code, **kwargs):
        response = {'status_code': status_code}
        try:
            response.update(kwargs)
            self.finish(response)
        except Exception as e:
            self.finish(response)