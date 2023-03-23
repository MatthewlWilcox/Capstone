import pandas as pd

data = pd.read_csv('src/Modeling/Test_find_stand_attend_na.csv')
data2 = pd.read_csv('data/final_datasets/data_standardized.csv')
data2_grouped = data2.groupby(['season', 'home_team'])['away_team'].count().sort_values().reset_index()
print(data2_grouped)
print(data2_grouped[data2_grouped['away_team']==1])
print(data.groupby(['division'])['away_team'].count().sort_values())
# print(data.groupby('season').count())