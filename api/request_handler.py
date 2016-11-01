"""
@Author: Hizaoui Mohamed Abdelkader
@Email-1: hizaoui.ma@gmail.com
@Email-2: hizaoui.mohamed.abdelkader@gmail.com
@created on: '11/1/16'
"""
from tornado.web import RequestHandler


class MDBRequestHandler(RequestHandler):
    def initialize(self):
        pass

    def post(self, db, collection):
        pass

    def get(self, db, collection, oid=None):
        pass

    def patch(self, db, collection, oid=None):
        pass

    def put(self, db, collection, oid=None):
        pass

    def delete(self, db, collection, oid=None):
        pass
