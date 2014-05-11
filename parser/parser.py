from service.match import FootballMatch

__author__ = 'aleksart'
from bs4 import BeautifulSoup


def parse_document(filename):
    f = open(filename)
    content = f.read()
    f.close()
    soup = BeautifulSoup(content)

    tour_results = parse_tour_results(soup)
    tour_num = 1
    matches_html = []
    all_matches = []
    for tour in tour_results:
        matches = tour.find_all('tr')
        for match in matches:
            info = dict()
            info['tour'] = tour_num
            time_info = match.find('td', 'name-td alLeft')
            time_info = time_info.text.split('|')
            info['date'] = time_info[0]
            info['time'] = time_info[1]
            host_info = match.find('td', 'owner-td')
            info['host'] = host_info.text
            guest_info = match.find('td', 'guests-td')
            info['guest'] = guest_info.text
            score_info = match.find('td', 'score-td')
            info['score'] = score_info.text
            info['visitors'] = match.find('td','padR alRight').text
            football_match = FootballMatch(info)
            print(football_match.score)
            all_matches.append(football_match)

            matches_html.append(match)


    return all_matches

def parse_tour_results(soup):

    headers = soup.find_all('h3', 'titleH3 bordered mB10')
    # print result
    tour_result = []
    for head in headers:
        tour_result.append(head.find_next_sibling('div').find('tbody'))
    return tour_result

def parse_match_results(row):
    print "parser works"