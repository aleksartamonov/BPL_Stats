from plotting.colors import colors
from service.match import FootballMatch

__author__ = 'aleksart'


class Team:
    def __init__(self, name, team_colors):
        self.name = name
        self.matches = []
        self.main_color = team_colors[0]
        self.add_color = team_colors[1]

    def add_match(self, football_match):
        self.matches.append(football_match)

    def get_results_from_match(self, football_match):
        if isinstance(football_match, FootballMatch):
            if self.name == football_match.host:
                scored_goals = football_match.score[0]
                missed_goals = football_match.score[1]
                if football_match.score[0] > football_match.score[1]:
                    points = 3
                elif football_match.score[0] == football_match.score[1]:
                    points = 1
                else:
                    points = 0
            elif self.name == football_match.guest:
                scored_goals = football_match.score[1]
                missed_goals = football_match.score[0]
                if football_match.score[0] < football_match.score[1]:
                    points = 3
                elif football_match.score[0] == football_match.score[1]:
                    points = 1
                else:
                    points = 0
            else:
                raise RuntimeError('team did not play that match')

            return points, scored_goals, missed_goals
        else:
            raise ValueError('football_match must be FootballMatch')


    def get_matches_result_in_date_range(self, begin, end, step):
        sorted_matches = sorted(self.matches, key=lambda x: x.datetime)
        timedelta = (end - begin) / step

        result = []

        for i in xrange(step):
            points = 0
            scored = 0
            missed = 0
            for match in sorted_matches:
                if begin + timedelta*i <= match.datetime < begin + timedelta*(i+1):
                    dp, ds, dm = self.get_results_from_match(match)
                    points += dp
                    scored += ds
                    missed += dm

            result.append([points, scored, missed])
        return result


class League:
    def __init__(self, name):
        self.name = name
        self.teams = dict()
        self.colors = colors[name]

    def add_team(self, team_name):
        self.teams[team_name] = Team(team_name, self.colors[team_name])


    def add_match(self, football_match):
        if football_match.guest not in self.teams.keys():
            self.add_team(football_match.guest)
        if football_match.host not in self.teams.keys():
            self.add_team(football_match.host)
        self.teams[football_match.host].add_match(football_match)
        self.teams[football_match.guest].add_match(football_match)
