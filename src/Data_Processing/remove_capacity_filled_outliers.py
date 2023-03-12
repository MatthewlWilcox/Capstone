import pandas as pd
data = pd.read_pickle('data/final_datasets/Total_data.pkl')
# data = data[['home_team', 'away_team', 'home_score', 'away_score', 'date_time', 'raw_attendance', 'capacity_filled', 'capacity', 'stadium', 'url']]
standard_dev = data['capacity_filled'].std()*3
mean_data = data['capacity_filled'].mean()
data = data[data['capacity_filled'] <= (mean_data+standard_dev)]
print(standard_dev)
print(mean_data)
# print(len(data['stadium'].unique()))

# grouped_data = data[['stadium', 'url', 'capacity']].groupby(['stadium', 'url']).mean().reset_index()

# print(grouped_data)
# google_urls = []
# for index, rows in grouped_data.iterrows():
    
#     stadium = rows['stadium'].replace(' ', '+') + '+capacity'
#     string = 'https://www.google.com/search?q=' + stadium
#     google_urls = google_urls + [string]

# grouped_data['google_urls'] = google_urls
# grouped_data.to_csv('error_stadium_capacisty.csv')
      
# data = data[data['capacity_filled']>1]
data = data.sort_values('capacity_filled', ascending = False)
print(data)
grouped_bet_dif_mean = data.groupby(['division', 'home_team']).mean().reset_index()
print(grouped_bet_dif_mean)
grouped_bet_dif_mean = grouped_bet_dif_mean[['division', 'home_team', 'raw_attendance']].rename(columns = {'raw_attendance': 'avg_attendance'})
grouped_bet_dif_std = data.groupby(['division', 'home_team']).std().reset_index()
print(grouped_bet_dif_mean)
grouped_bet_dif_std = grouped_bet_dif_std[['division', 'home_team', 'raw_attendance']].rename(columns = {'raw_attendance': 'std_attendance'})

data = pd.merge(data, grouped_bet_dif_mean, on = ['division', 'home_team'])
data = pd.merge(data, grouped_bet_dif_std, on = ['division', 'home_team'])

data.to_pickle('data/final_datasets/dataset_no_over_capacity.pkl')
data.to_csv('data/final_datasets/dataset_no_over_capacity.csv')