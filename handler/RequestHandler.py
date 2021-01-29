from http.server import BaseHTTPRequestHandler
from controller.Controller import Controller


class RequestHandler(BaseHTTPRequestHandler):
    routes = {
        "/": Controller.root
    }

    def do_GET(self):
        try:
            controller_method = self.routes[self.path]
            output = controller_method(self)
            self.write(200, output)
        except KeyError:
            self.write(404, "Not Found")

    def do_POST(self):
        raise NotImplementedError

    def write(self, code, output):
        self.send_response_only(code)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(output, 'utf-8'))

