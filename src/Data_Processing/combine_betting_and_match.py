import pandas as pd
import pickle

match_data = pd.read_pickle('data/Data_to_change/match_data_updated_date.pkl')
betting_data = pd.read_pickle('data/Data_to_change/betting_data_updated_date.pkl')
print(match_data.columns)
print(betting_data.columns)


merged_df = pd.merge(match_data, betting_data, left_on = ['date', 'home_team', 'away_team'], right_on = ['Date', 'HomeTeam', 'AwayTeam'])


merged_df.to_pickle('data/Data_to_change/betting_and_match_data.pkl')
merged_df.to_csv('data/Data_to_change/betting_and_match_data.csv')