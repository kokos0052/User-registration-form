import json
import os

import tornado.ioloop
import tornado.web
import pika


class FormHandler(tornado.web.RequestHandler):
    def post(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
        connection_parameters = pika.ConnectionParameters(os.environ.get('queue_host'), os.environ.get('queue_port'))
        connection = pika.BlockingConnection(connection_parameters)
        channel = connection.channel()

        channel.queue_declare(queue='queue')

        message = json.loads(self.request.body)
        channel.basic_publish(
            exchange='', routing_key='queue', body=json.dumps(message))

        connection.close()


def make_app():
    return tornado.web.Application([
        (r"/send", FormHandler),
    ],
        debug=True,
        autoreload=True)


if __name__ == '__main__':
    app = make_app()
    port = os.environ.get('port')
    app.listen(port)
    print('Server launched')
    tornado.ioloop.IOLoop.current().start()
