import pytz

__author__ = 'aleksart'

from datetime import date, datetime, time
tz = pytz.timezone('Europe/London')


class FootballMatch:
    def __init__(self, initial_dict):
        dmy = initial_dict['date'].split('.')
        self.date = date(int(dmy[2]), int(dmy[1]), int(dmy[0]))
        hm = initial_dict['time'].split(':')
        self.time = time(int(hm[0]), int(hm[1]))
        self.datetime = datetime.combine(self.date, self.time)

        self.datetime.replace(tzinfo=tz)
        self.host = initial_dict['host']
        self.guest = initial_dict['guest']
        try:
            self.visitors = int(initial_dict['visitors'])
        except ValueError:
            self.visitors = 0
        self.score = [int(i) for i in initial_dict['score'].split(':')]
        self.tour = int(initial_dict['tour'])

    def __str__(self):
        res_str = self.host + ' : ' + self.guest + ' - '
        res_str += ':'.join([str(i) for i in self.score]) + ' - '
        res_str += self.datetime.strftime("%A, %d. %B %Y %I:%M%p")
        return res_str