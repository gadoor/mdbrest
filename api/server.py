"""
@Author: Hizaoui Mohamed Abdelkader
@Email-1: hizaoui.ma@gmail.com
@Email-2: hizaoui.mohamed.abdelkader@gmail.com
@created on: '11/1/16'
"""
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from motor import motor_tornado

from api import get_application


def main(port=6767):
    try:
        app = get_application()
        http_server = HTTPServer(app)
        http_server.bind(port)
        http_server.start()
        app.settings['client'] = motor_tornado.MotorClient("mongodb://192.168.122.10:27017")
        IOLoop.current().start()
    except KeyboardInterrupt:
        IOLoop.current().stop()

if __name__ == '__main__':
    main()