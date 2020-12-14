from src.bovada_api import BovadaAPI
from src.game import Game


class BettingOdds:
    def __init__(self):
        self._api = BovadaAPI().get_betting_odds()[0]

    def get_events(self):
        return self._api['events']

    @staticmethod
    def get_competitors(game):
        return game['competitors']

    @staticmethod
    def get_display_groups(game):
        return game['displayGroups']

    @staticmethod
    def get_name(team):
        return team['name']

    @staticmethod
    def is_home_team(team):
        return bool(team['home'])

    @staticmethod
    def get_markets(display_group):
        return display_group['markets']

    def build_odds_sheet(self):
        slate = []
        for event in self.get_events():
            game = Game()
            slate.append(game)
            for team in self.get_competitors(event):
                if self.is_home_team(team):
                    game.set_home_team(self.get_name(team))
                else:
                    game.set_away_team(self.get_name(team))
            for display_group in self.get_display_groups(event):
                for market in self.get_markets(display_group):
                    if market['description'] == 'Moneyline':
                        for betting_odd in market['outcomes']:
                            if betting_odd['description'] == game.get_home_team():
                                game.set_home_money_line(betting_odd['price']['american'])
                            else:
                                game.set_away_money_line(betting_odd['price']['american'])
                    elif market['description'] == 'Point Spread':
                        for betting_odd in market['outcomes']:
                            if betting_odd['description'] == game.get_home_team():
                                game.set_home_spread(betting_odd['price']['handicap'])
                            else:
                                game.set_away_spread(betting_odd['price']['handicap'])
                    elif market['description'] == 'Total':
                        for betting_odd in market['outcomes']:
                            if betting_odd['description'] == 'Over':
                                game.set_over(betting_odd['price']['handicap'])
                            else:
                                game.set_under(betting_odd['price']['handicap'])
        return slate
                
                


                


