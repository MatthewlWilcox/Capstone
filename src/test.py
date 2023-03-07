import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


div_dict = {'D1':'Bundesliga', 'D2': '2. Bundesliga', 'E0':'Premier League', 'E1':'Championship', 
            'E2':'League 1', 'E3':'Leauge 2','SP1':'La Liga Primera', 'SP2':'La Liga Segunda',
              'B1':'Jupiler League', 'F1':'Ligue 1','F2':'Ligue 2','I1':'Serie A','I2':'Seire B', 
              'SC0':'Scotish Premier League', 'SC1':'Scotish Division 1', 'T1':'Fubol Ligi 1'}

total_data_set = pd.read_pickle('d:/Python Work/Capstone/data/final_datasets/total_data.pkl')


impact_data = total_data_set[total_data_set.division != 'SC2']
impact_data = impact_data[['home_team', 'away_team', 'date_time', 'division', 'raw_attendance', 'capacity_filled']]
impact_data['year']= impact_data['date_time'].dt.year
impact_data = impact_data.dropna()

average_team_attendance = impact_data.groupby(['year', 'home_team']).mean().reset_index().rename(columns = {'raw_attendance':'avg_raw_attendance', 'capacity_filled':'avg_capacity_filled'})
standard_dev_attendance = impact_data.groupby(['year', 'home_team']).std().reset_index().rename(columns = {'raw_attendance':'std_raw_attendance', 'capacity_filled':'std_capacity_filled'})


# print(average_team_attendance)
# print(standard_dev_attendance)
avg_df = pd.merge(impact_data,average_team_attendance, on = ['year','home_team'])
avg_df = pd.merge(avg_df, standard_dev_attendance, on = ['year', 'home_team'])
# print(avg_df)
# print(avg_df.isna().sum())
avg_df['away_team_impact'] = avg_df['raw_attendance'] - avg_df['avg_raw_attendance']
avg_df['attendance_zscore'] = (avg_df['raw_attendance']- avg_df['avg_raw_attendance'])/avg_df['std_raw_attendance']

# print(avg_df.sort_values('attendance_zscore'))
# avg_df.to_csv('src/Teams_impact/avg_df.csv')
away_team_impact = avg_df.groupby(['away_team', 'division']).mean().reset_index()
away_team_impact = away_team_impact[['away_team', 'attendance_zscore', 'away_team_impact','division']].reset_index()



import ipywidgets as widgets
leagues_impact_away_team = away_team_impact
# .sort_values('division').replace({'division':div_dict})
divisions_list = list(set(leagues_impact_away_team.division.values.tolist()))
print(divisions_list)
print(sorted(divisions_list))

divisions_list = [div_dict.get(item,item) for item in divisions_list]
print(divisions_list)


dd = widgets.Dropdown(
  options = divisions_list,
  value = divisions_list[0],
  description = 'Select a Division'
)

def draw_plot(div):
    df = away_team_impact[away_team_impact['division']==div]

    p = sns.barplot(data = df,
                     x = 'attendance_zscore', y = 'away_team', hue = 'division', dodge = False)

widgets.interact(draw_plot, div = dd)

