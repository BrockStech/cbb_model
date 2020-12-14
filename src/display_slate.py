from src.betting_odds import BettingOdds


def display():
    slate = BettingOdds().build_odds_sheet()
    for game in slate:
        if game.get_home_team() and game.get_away_team():
            print(f'{game.get_home_team():25} {game.get_home_spread():10} {game.get_home_money_line():10}'
                  f'O{game.get_over():10} \n'
                  f'{game.get_away_team():25} {game.get_away_spread():10} {game.get_away_money_line():10}'
                  f'U{game.get_under():10}')
