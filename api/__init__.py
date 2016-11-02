"""
@Author: Hizaoui Mohamed Abdelkader
@Email-1: hizaoui.ma@gmail.com
@Email-2: hizaoui.mohamed.abdelkader@gmail.com
@created on: '11/1/16'
"""
from tornado.web import Application

from api.request_handler import MDBRequestHandler


def get_application():
    app = Application([(r'/', MDBRequestHandler),
                       (r'/(?P<db>[^\/]+)/(?P<collection>[^\/]+)', MDBRequestHandler),
                       (r'/(?P<db>[^\/]+)/(?P<collection>[^\/]+)/(?P<oid>[^\/]+)', MDBRequestHandler)])

    return app