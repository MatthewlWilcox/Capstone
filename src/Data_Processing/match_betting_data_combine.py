import pandas as pd
import pickle
from re import sub
def snake_case(s):
  return '_'.join(
    sub('([A-Z][a-z]+)', r' \1',
    sub('([A-Z]+)', r' \1',
    s.replace('-', ' '))).split()).lower()


match_data = pd.read_csv('data/RAWDATA/RAW_match_data.csv')
betting_data = pd.read_csv('data/RAWDATA/RAW_betting_data.csv')

betting_data = betting_data[betting_data['HomeTeam'].notna()]
match_data_team_list = match_data['home_team'].unique()
match_data_team_list = list(map(snake_case, match_data_team_list))
betting_data_team_list = betting_data['HomeTeam'].unique()

betting_data_team_list =list(map(snake_case, betting_data_team_list))
match_set = set(match_data_team_list)
betting_set = set(betting_data_team_list)

dif = list(match_set.symmetric_difference(betting_set))




match_data_list_error_data = []
betting_data_list_error_data = []

for i in dif:
  if i in match_data_team_list:
    match_data_list_error_data.append(i)

for i in dif:
  if i in betting_data_team_list:
    betting_data_list_error_data.append(i)

print(match_data_list_error_data)
print("#"*50)
print(betting_data_list_error_data)
print(len(match_data_list_error_data))
print(len(betting_data_list_error_data))

with open('src/Data_Processing/match_error_teams.pkl', 'wb') as pick:
  pickle.dump(match_data_list_error_data, pick)
with open('src/Data_Processing/betting_error-team.pkl', 'wb') as pick:
  pickle.dump(betting_data_list_error_data, pick)