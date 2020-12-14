class Game:
    def __init__(self):
        self._home_team = None
        self._away_team = None
        self._home_spread = ''
        self._away_spread = ''
        self._home_money_line = ''
        self._away_money_line = ''
        self._over = ''
        self._under = ''

    def get_home_team(self):
        return self._home_team

    def set_home_team(self, team):
        self._home_team = team

    def get_away_team(self):
        return self._away_team

    def set_away_team(self, team):
        self._away_team = team

    def get_home_spread(self):
        return self._home_spread

    def set_home_spread(self, spread):
        self._home_spread = spread

    def get_away_spread(self):
        return self._away_spread

    def set_away_spread(self, spread):
        self._away_spread = spread

    def get_home_money_line(self):
        return self._home_money_line

    def set_home_money_line(self, money_line):
        self._home_money_line = money_line

    def get_away_money_line(self):
        return self._away_money_line

    def set_away_money_line(self, money_line):
        self._away_money_line = money_line

    def get_over(self):
        return self._over

    def set_over(self, over):
        self._over = over

    def get_under(self):
        return self._under

    def set_under(self, under):
        self._under = under



