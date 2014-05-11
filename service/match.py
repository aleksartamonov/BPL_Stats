__author__ = 'aleksart'

from datetime import date, datetime, time


class FootballMatch:
    def __init__(self, initiat_dict):
        dmy = initiat_dict['date'].split('.')
        self.date = date(int(dmy[2]), int(dmy[1]), int(dmy[0]))
        hm = initiat_dict['time'].split(':')
        self.time = time(int(hm[0]), int(hm[1]))
        self.datetime = datetime.combine(self.date, self.time)
        self.host = initiat_dict['host']
        self.guest = initiat_dict['guest']
        try:
            self.visitors = int(initiat_dict['visitors'])
        except ValueError:
            self.visitors = 0
        self.score = [int(i) for i in initiat_dict['score'].split(':')]
        self.tour = int(initiat_dict['tour'])