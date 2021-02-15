import os
from model.DateProvider import *

class Controller:

    def root(self):
        base_path = os.path.dirname(os.path.realpath(__file__)) + '/../view/'
        body = ''
        with open(base_path + 'hello.html', 'r') as file:
            body = file.read()
        #call model and get today's date
        todays_date = getStringDate()
        body = body.replace('${todayDate}', todays_date)
        return body

