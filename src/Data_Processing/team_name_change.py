import pandas as pd
import pickle
from re import sub


def snake_case(s):
  return '_'.join(
    sub('([A-Z][a-z]+)', r' \1',
    sub('([A-Z]+)', r' \1',
    s.replace('-', ' '))).split()).lower()

betting_data = pd.read_csv('data/RAWDATA/RAW_betting_data.csv')
match_data =  pd.read_csv('data/RAWDATA/RAW_match_data.csv')
with open('src/Data_Processing/key_dictionary.pkl', 'rb') as pick:
    key_dict = pickle.load(pick)
betting_data['HomeTeam'] =betting_data['HomeTeam'].apply(str)
betting_data['HomeTeam'] =betting_data['HomeTeam'].apply(snake_case)
betting_data['AwayTeam'] =betting_data['AwayTeam'].apply(str)
betting_data['AwayTeam'] =betting_data['AwayTeam'].apply(snake_case)

betting_data['HomeTeam'] = betting_data['HomeTeam'].replace(key_dict)
betting_data['AwayTeam'] = betting_data['AwayTeam'].replace(key_dict)

match_data['home_team'] =match_data['home_team'].apply(str)
match_data['home_team'] =match_data['home_team'].apply(snake_case)
match_data['away_team'] =match_data['away_team'].apply(str)
match_data['away_team'] =match_data['away_team'].apply(snake_case)

match_data['Hohome_teammeTeam'] = match_data['home_team'].replace(key_dict)
match_data['away_team'] = match_data['away_team'].replace(key_dict)

betting_data.to_pickle('data/Data_to_change/betting_data_updated_names.pkl')
match_data.to_pickle('data/Data_to_change/match_data_updated_names.pkl')
