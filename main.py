# -*- coding: utf-8 -*-
from parser.parser import parse_document as parse_document
from service.team import League
from datetime import date, time, datetime

if __name__ == "__main__":
    stat_file = "calendar.html"
    print "main block"
    matches = parse_document(stat_file)

    bpl = League('BPL')

    for match in matches:
        bpl.add_match(match)

    mc_name = 'Манчестер Сити'
    mc = bpl.teams[mc_name]

    begin = datetime(2013, 8, 14, 00, 00)
    end = datetime(2014, 5, 12, 00, 00)
    print begin.strftime("%A, %d. %B %Y %I:%M%p") ,'-',end.strftime("%A, %d. %B %Y %I:%M%p")
    for achieve in mc.get_matches_result_in_date_range(begin, end, 12):
        print ' - '.join([str(i) for i in achieve])

    output = open("output.dat", "w")
    for m in matches:
        output.write(str(m)+'\n')
    output.close()