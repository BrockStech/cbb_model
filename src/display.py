from src.prediction import Prediction


def display():
    prediction = Prediction()
    prediction.make()
    for game in prediction.betting_slate:
        print(f'{game.get_home_team():25} {game.get_home_spread():10} {game.get_home_money_line():10}'
              f'O{game.get_over():10} \n'
              f'{game.get_away_team():25} {game.get_away_spread():10} {game.get_away_money_line():10}'
              f'U{game.get_under():10} \n')

    # TODO: display our picks
