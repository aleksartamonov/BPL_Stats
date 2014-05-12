__author__ = 'aleksart'
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import matplotlib.dates as mdates
from matplotlib import rc
import Image
img = Image.open('logo.png')
rc('font', **{'family':'sanserif'})
rc('text', usetex=True)
rc('text.latex', unicode=True)
rc('text.latex', preamble='\usepackage[utf8]{inputenc}')
rc('text.latex', preamble='\usepackage[russian]{babel}')


def point_progress_in_time(league, output):
    ax = plt.subplot('111',axisbg='#000044')
    plots = []

    for team in league.teams.values():
        points = []
        date = []

        for i in range((league.end - league.start).days + 10):
            now = league.start + timedelta(days=i)
            date.append(now)
            points.append(team.get_matches_result_in_date_range(league.start, now, 1)[0][0])
        #print team.name
        #print points
        # x = [datetime.strptime(d, '%m/%d/%Y').date() for d in date]
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%Y'))
        plt.gca().xaxis.set_major_locator(mdates.MonthLocator())
        ax.plot(date, points, '-o', color=team.add_color, lw=4, alpha=0.8, ms=3, mfc=team.main_color, label=team.name.decode('utf-8').strip())


    legend = plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
    for text in legend.get_texts():
        text.set_color("white")
    frame = legend.get_frame()
    frame.set_color('#000044')
    plt.subplots_adjust(left=0.1, right=0.8, top=0.9, bottom=0.3)
    plt.gcf().autofmt_xdate()
    #plt.show()
    fig = plt.gcf()

    fig.set_size_inches(18.5,10.5)
    plt.savefig(output,dpi = 300)