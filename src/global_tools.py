import pandas as pd


def clean(team_name):
    return team_name.strip().split(' (')[0]


def read_data_and_convert_to_data_frame():
    return pd.read_csv('../data/model_data.csv', header=0)
