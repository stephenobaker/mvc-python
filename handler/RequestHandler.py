from http.server import BaseHTTPRequestHandler
from controller.Controller import Controller


class RequestHandler(BaseHTTPRequestHandler):
    routes = {
        "/": Controller.root
    }

    def do_GET(self):
        controller_method = self.lookupRoute()

        output = controller_method(self)

        self.write(output)

    def do_POST(self):
        raise NotImplementedError

    def write(self, output):
        self.send_response_only(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(output, 'utf-8'))

    def lookupRoute(self):
        try:
            controller_method = self.routes[self.path]
        except KeyError:
            self.send_response_only(404)
            self.end_headers()
        return controller_method
