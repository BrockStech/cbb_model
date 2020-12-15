import numpy as np
import pandas as pd
from sportsreference.ncaab.teams import Teams
from sportsreference.ncaab.schedule import Schedule
from urllib.error import HTTPError


class Model:

    def __init__(self):
        self.df = pd.DataFrame()
        self.teams = pd.DataFrame()

    # Note: This process takes multiple hours to run
    def build(self):
        self.teams = Teams(2020).dataframes['abbreviation']
        self.pull_team_stats()
        self.clean_data()
        self.df.to_excel('model_data.xlsx')
        self.calculate()

    def pull_team_stats(self):
        for team in self.teams:
            for year in range(2015, 2021):
                try:
                    self.df = self.df.append(Schedule(team, year).dataframe_extended)
                except HTTPError:
                    print("HTTP Error")

    def clean_data(self):
        self.df = self.df.drop(columns=['home_ranking', 'away_ranking', 'date', 'location', 'losing_abbr',
                                        'winning_abbr', 'losing_name', 'winning_name', 'winner']).dropna()

    def calculate(self):
        r_squared_array = {}
        for column in self.df:
            correlation_matrix = np.corrcoef(self.df['home_points'], self.df[column].astype('float64'))
            r_squared = correlation_matrix[0, 1] ** 2
            r_squared_array[column] = r_squared
        print(sorted(r_squared_array.items(), key=lambda x: x[1], reverse=True))
