import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
data = pd.read_pickle('data/final_datasets/Total_data.pkl')
data = data[data.division != 'SC2']
df = data[['home_team', 'away_team', 'date_time', 'division', 'raw_attendance', 'capacity_filled']]
df['year']= df['date_time'].dt.year
df = df.dropna()

average_team_attendance = df.groupby(['year', 'home_team']).mean().reset_index().rename(columns = {'raw_attendance':'avg_raw_attendance', 'capacity_filled':'avg_capacity_filled'})
standard_dev_attendance = df.groupby(['year', 'home_team']).std().reset_index().rename(columns = {'raw_attendance':'std_raw_attendance', 'capacity_filled':'std_capacity_filled'})


# print(average_team_attendance)
# print(standard_dev_attendance)
avg_df = pd.merge(df,average_team_attendance, on = ['year','home_team'])
avg_df = pd.merge(avg_df, standard_dev_attendance, on = ['year', 'home_team'])
# print(avg_df)
# print(avg_df.isna().sum())
avg_df['away_team_impact'] = avg_df['raw_attendance'] - avg_df['avg_raw_attendance']
avg_df['attendance_zscore'] = (avg_df['raw_attendance']- avg_df['avg_raw_attendance'])/avg_df['std_raw_attendance']

# print(avg_df.sort_values('attendance_zscore'))
# avg_df.to_csv('src/Teams_impact/avg_df.csv')
away_team_impact = avg_df.groupby('away_team').mean().reset_index()
away_team_impact = away_team_impact[['away_team', 'attendance_zscore', 'away_team_impact']].sort_values('attendance_zscore', ascending=False).reset_index()

# print(away_team_impact.head(50))

div_dict = {'D1':'Bundesliga', 'D2': '2. Bundesliga', 'E0':'Premier League', 'E1':'Championship', 
            'E2':'League 1', 'E3':'Leauge 2','SP1':'La Liga Primera', 'SP2':'La Liga Segunda',
              'B1':'Jupiler League', 'F1':'Ligue 1','F2':'Ligue 2','I1':'Serie A','I2':'Seire B', 
              'SC0':'Scotish Premier League', 'SC1':'Scotish Division 1', 'T1':'Fubol Ligi 1'}

div_avg = df.groupby('division').median().reset_index().sort_values('capacity_filled', ascending = False)
div_avg = div_avg.replace({'division':div_dict})
print(div_avg['division'])

# away_team_impact.to_csv('src/Teams_impact/away_team_impact.csv')


division_fig = sns.barplot(data = div_avg, y='division', x= 'capacity_filled')
# plt.bar(div_avg['division'], div_avg['capacity_filled'],  align = 'center')
plt.title('Average Capacity Filled By League')
plt.xlabel('Average Capacity Filled')
plt.ylabel('League')

plt.show()