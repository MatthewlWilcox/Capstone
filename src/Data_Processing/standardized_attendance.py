import pandas as pd
from datetime import datetime as dt
data = pd.read_pickle('data/final_datasets/Total_data.pkl')
season = []
for index, rows in data.iterrows():
    match_day = dt.strptime(rows['date'], '%Y-%m-%d')
    # print(match_day)
    year = int(dt.strftime(match_day, '%Y'))
    month_day = dt.strftime(match_day, '%m-%d')
    # print(int(year))
    # print(type(year))
    # print(month_day)
    cutoff_date = dt.strftime(dt(2014,7,14), '%m-%d')
    if month_day > cutoff_date:
        year = year +1
        season = season + [year]

    else:
        season = season + [year]


data['season'] = season

data_std = data.groupby(['home_team', 'season']).std().reset_index()
data_std = data_std[['home_team', 'season', 'raw_attendance']].rename(columns = {'raw_attendance':'std_attend'})
data_mean = data.groupby(['home_team', 'season']).mean().reset_index()
data_mean = data_mean[['home_team', 'season', 'raw_attendance']].rename(columns = {'raw_attendance': 'mean_attend'})
data = pd.merge(data, data_mean, on = ['home_team', 'season'])
data = pd.merge(data, data_std, on= ['home_team', 'season'])
data['standard_attend'] = (data['raw_attendance']-data['mean_attend'])/ data['std_attend']

data.to_pickle('data/final_datasets/data_standardized.pkl')
data.to_csv('data/final_datasets/data_standardized.csv')

print(data)