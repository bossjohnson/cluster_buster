# load environment variables
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

import BaseHTTPServer

import kube_api


class My_Handler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_GET(self):
        print 'got GET request to path: %s' % self.path

        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()

        pods = kube_api.get_pods()

        self.wfile.write(pods)

def run(server_class=BaseHTTPServer.HTTPServer,
        handler_class=BaseHTTPServer.BaseHTTPRequestHandler):
    print 'running'
    server_address = ('', 8000)
    httpd = server_class(server_address, My_Handler)
    httpd.serve_forever()


if __name__ == '__main__':
    run()
