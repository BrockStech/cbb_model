import pickle
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from src.betting_odds import BettingOdds
from src.global_tools import *


class Prediction:
    def __init__(self):
        self.model = LinearRegression()
        self.df = pd.DataFrame()
        self.betting_slate = []

    def make(self):
        self._import_model()
        self.df = read_data_and_convert_to_data_frame()
        self._append_team_name_column()
        self._build_slate()
        self._predict_slate()

    def _import_model(self):
        self.model = pickle.load(open('../data/model.sav', 'rb'))

    def _append_team_name_column(self):
        self.df['home_team'] = self.df.apply(lambda row: self.home_team(row), axis=1)
        self.df['away_team'] = self.df.apply(lambda row: self.away_team(row), axis=1)

    def _build_slate(self):
        self.betting_slate = BettingOdds().build_odds_sheet()

    def _predict_slate(self):
        for game in self.betting_slate:
            # TODO: Add model
            # self.df.loc[self.df['home_team'] == test_team]
            print(clean(game.get_home_team()) + " - " + clean(game.get_away_team()) + "\n")

    # TODO: Create model accuracy test
    def _test_prediction(self):
        data = pd.read_csv('../data/model_data.csv', header=0)

        # Make sure these attributes line up with the training data (model.py)
        attributes = ['away_defensive_rating', 'home_offensive_rating',
                      'home_true_shooting_percentage', 'home_effective_field_goal_percentage']

        test = data.sample(frac=0.75, random_state=1)

        x_test = test[attributes]
        y_test = test['home_points']

        predictions = self.model.predict(x_test)
        mae = mean_absolute_error(y_test, predictions)
        print(predictions)
        print(mae)

    @staticmethod
    def home_team(row):
        if row['winner'] == 'Home':
            return clean(row['winning_name'])
        elif row['winner'] == 'Away':
            return clean(row['losing_name'])
        else:
            return 'None'

    @staticmethod
    def away_team(row):
        if row['winner'] == 'Away':
            return clean(row['winning_name'])
        elif row['winner'] == 'Home':
            return clean(row['losing_name'])
        else:
            return 'None'
