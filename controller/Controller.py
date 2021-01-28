import os


class Controller:

    def root(self):
        base_path = os.path.dirname(os.path.realpath(__file__)) + '/../view/'
        with open(base_path + 'hello.html', 'r') as file:
            return file.read()
