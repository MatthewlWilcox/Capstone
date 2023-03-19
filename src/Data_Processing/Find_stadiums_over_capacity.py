import pandas as pd
import os 
import webbrowser
from time import sleep

data = pd.read_pickle('data/final_datasets/Total_data.pkl')
# data = data[data['capacity_filled']>1]
stadiums = data.groupby('stadium').mean().reset_index()
stadiums = stadiums[['stadium', 'capacity']]
stadiums['stadium_rename']= stadiums['stadium'].str.replace(' ', '+')
stadiums['url'] = 'https://www.google.com/search?q=' + stadiums['stadium_rename'] + '+Capacity+fotmob'
stadiums = stadiums.drop(columns = 'stadium_rename')
print(stadiums)


new_capacity = []
source = []
# x = input()
for index, rows in stadiums.iterrows():
    os.system('cls')
    temp_stadium_name = rows['stadium']
    data_stadium_filter_df = data[data['stadium'] == temp_stadium_name]
    data_stadium_filter_df = data_stadium_filter_df.groupby(['home_team', 'stadium']).mean().reset_index()
    data_stadium_filter_df = data_stadium_filter_df[['home_team', 'stadium']]
    stadium_names = data_stadium_filter_df['home_team'].unique()
    print('Stadium: ',rows['stadium'], '\nTeams: ', stadium_names, '\nCapacity: ', rows['capacity'])
    webbrowser.open(rows['url'])
    update_capacity = input('Input New Capacity:') or rows['capacity']
    input_source = input('Input Source:') or ' '
    print(update_capacity)
    new_capacity = new_capacity + [update_capacity]
    source = source + [input_source]

    sleep(1)

stadiums['new_capacity'] = new_capacity
stadiums['source']= source
print(stadiums)
stadiums.to_csv('new_capacity_stadiums.csv')
stadiums.to_pickle('new_capacity_stadiums.pkl')