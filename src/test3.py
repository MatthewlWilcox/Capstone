import pandas as pd
data = pd.read_pickle('data/final_datasets/Total_data.pkl')
data = data[['home_team', 'away_team', 'home_score', 'away_score', 'date_time', 'raw_attendance', 'capacity_filled', 'capacity', 'stadium', 'url']]
standard_dev = data['capacity_filled'].std()*3
mean_data = data['capacity_filled'].mean()
# data = data[data['capacity_filled'] <= (mean_data+standard_dev)]
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
      
data = data[data['capacity_filled']>1.1]
data3 = data.groupby('stadium').mean().reset_index()
print(data3[['stadium', 'raw_attendance']])
# data = data.sort_values('capacity_filled', ascending = False)
# print(data)
# data.to_csv('test_bad_data_capacity.csv')