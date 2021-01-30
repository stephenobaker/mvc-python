import threading
import unittest
from http.server import HTTPServer

import requests

from app.handler.RequestHandler import RequestHandler


class MvcAcceptanceTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.server = HTTPServer(('', 8080), RequestHandler)
        cls.thread = threading.Thread(target=cls.server.serve_forever)
        cls.thread.start()

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()

    def test__root_path__should_return_hello_world(self):
        url = "http://localhost:8080"
        response = requests.get(url)

        self.assertEqual(200, response.status_code)
        self.assertEqual(True, response.text.__contains__("Hello World"))

    def test__bad_path__should_return_not_found(self):
        url = "http://localhost:8080/bad"
        response = requests.get(url)

        self.assertEqual(404, response.status_code)
        self.assertEqual(True, response.text.__contains__("Not Found"))


if __name__ == '__main__':
    unittest.main()
