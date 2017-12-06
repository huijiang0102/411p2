import tornado.web
import tornado.websocket
import tornado.httpserver
import tornado.ioloop
import socketserver.buffer
# from tornado.options import define, options

clients = dict()

class WebServer(object):
    def __init__(self, port=8080):

        # define("port", default=port, help="Run on the given port", type=int)
        app = tornado.web.Application([
        (r'/', IndexHandler),
        (r'/(?P<Id>\w*)', MyWebSocketHandler),
        (r"/static/(.*)", tornado.web.StaticFileHandler, {'path':'static/'}),
        ])
        print("DSP Control Application | Browse to <IP>:"+str(port)+" and have fun!")
        tornado.options.parse_command_line()
        app.listen(8080)
        print("listening now")
        tornado.ioloop.IOLoop.instance().start()

class IndexHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def get(self, **kwargs):
        pass

class MyWebSocketHandler(tornado.websocket.WebSocketHandler):

    def open(self, *args, **kwargs):
        self.id = kwargs['Id']
        self.stream.set_nodelay(True)
        clients[self.id] = {"id": self.id, "object": self}

    def on_message(self, message):
        print("Client %s received a message: %s" % (message))
        self.write_message('Copy that')
        self.write_message(message)

    def on_close(self):
        if self.id in clients:
            del clients[self.id]

    def check_origin(self, origin):
        return True

if __name__ == "__main__":

    server = WebServer()

