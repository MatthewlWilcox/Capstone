import pandas as pd

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
match_set = set(match_data)
betting_set = set(betting_data)

dif = list(match_set.symmetric_difference(betting_set))

# print(dif)
print(match_set)
# print(match_data_team_list)
# print(betting_data_team_list)
# print(len(match_data_team_list))
# print(len(betting_data_team_list))