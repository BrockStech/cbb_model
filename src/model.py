import numpy as np
from sportsreference.ncaab.teams import Teams
from sportsreference.ncaab.schedule import Schedule
from urllib.error import HTTPError
from sklearn import preprocessing
from sklearn.linear_model import LinearRegression
from src.global_tools import *
import pickle


class Model:
    def __init__(self):
        self.df = pd.DataFrame()
        self.teams = pd.DataFrame()
        self.model = LinearRegression()

    # Note: This process takes multiple hours to run
    def build_data_sheet(self):
        self.teams = Teams(2020).dataframes['abbreviation']
        self._pull_team_stats()
        self.df.to_excel('../data/model_data_v2.xlsx')

    def build_model_attributes(self):
        self.df = read_data_and_convert_to_data_frame()
        self._clean_data()
        self.df = pd.DataFrame(preprocessing.scale(self.df), columns=self.df.columns)
        self._calculate()

    def build_model(self):
        self.df = read_data_and_convert_to_data_frame()
        self._clean_data()
        self._train()
        pickle.dump(self.model, open('../data/model.sav', 'wb'))

    def _pull_team_stats(self):
        for year in range(2015, 2021):
            for team in self.teams:
                try:
                    self.df = self.df.append(Schedule(team, year).dataframe_extended)
                except HTTPError:
                    print("HTTP Error")

    def _train(self):
        attributes = ['away_defensive_rating', 'home_offensive_rating',
                      'home_true_shooting_percentage', 'home_effective_field_goal_percentage']

        train = self.df.sample(frac=0.75, random_state=1)
        x_train = train[attributes]
        y_train = train['home_points']
        self.model.fit(x_train, y_train)

    def _clean_data(self):
        self.df = self.df.drop(columns=['team_date', 'home_ranking', 'away_ranking', 'date', 'location', 'losing_abbr',
                                        'winning_abbr', 'losing_name', 'winning_name', 'winner']).dropna()

    def _calculate(self):
        r_squared_array = {}
        for column in self.df:
            correlation_matrix = np.corrcoef(self.df['home_points'], self.df[column].astype('float64'))
            r_squared_array[column] = correlation_matrix[0, 1] ** 2
        print(sorted(r_squared_array.items(), key=lambda x: x[1], reverse=True))
