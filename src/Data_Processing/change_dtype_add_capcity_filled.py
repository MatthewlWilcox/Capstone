import pandas as pd
import numpy as np
import re
from datetime import datetime, time

data = pd.read_pickle('data/Data_to_change/complete_data_2010_2019_shrunk.pkl')

for col in data.columns:
    print(col)

data = data.rename(columns = {'attendance':'raw_attendance'})
data['Capacity'] = data['Capacity'].astype(str)

data.loc[data.url == 'https://www.worldfootball.net/venues/mersin-arena-mersin/', 'Capacity'] = '25534'
data.loc[data.url == 'https://www.worldfootball.net/venues/stade-paul-lignon-rodez/', 'Capacity'] = '5955'


# df2 = data[data['away_score'].str.contains('\d')]
# print(df2)
# df2.to_csv('src/Data_processing/missing_capicty.csv')

data = data[data['raw_attendance'].str.contains('\d')]
data['raw_attendance'] = data['raw_attendance'].astype(float)
data['Capacity'] = data['Capacity'].astype(float)

def remove_non_numberics(s):
    return re.sub('[^0-9]', '', s)

data['away_score'] = data['away_score'].apply(lambda x: re.sub('[^0-9]', '', x))

# print(df2['Capacity'])
# for index, row in data.iterrows():
#     if row['check_raw'] == 'str'
# print(data[['Capacity', 'raw_attendance']])


# print(data[['raw_attendance', 'Capacity']].dtypes)
data['capacity_filled'] = data['raw_attendance']/data['Capacity']
# data['capacity_filled'] = data['capacity_filled'].round(4)


# Alter Data types:
data= data.rename(columns={'stadium_y':'stadium', 'City':'city', 'Country':'country', 'Capacity':'capacity', 'Div':'division'})
data['home_score']= data['home_score'].astype(int)
data['away_score'] = data['away_score'].astype(int)
data['date'] = data['date'].astype(str)
# data['time'] = data['time'].apply(lambda x: datetime.strptime(x, '%H:%M'))
data['date_time'] = data.apply(lambda row: pd.to_datetime(str(row['date']) + ' ' + str(row['time'])),axis = 1)
data['raw_attendance']= data['raw_attendance'].astype(int)
print(data)

data.to_pickle('data/final_datasets/Total_data.pkl')

data.to_csv('data/final_datasets/Total_data.csv')