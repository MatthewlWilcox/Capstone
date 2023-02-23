import pandas as pd
import numpy as np
data = pd.read_pickle('data/Data_to_change/complete_data_before_2019.pkl')


for col in data.columns:
    print(col)

data = data.rename(columns = {'attendance':'raw_attendance'})
data['Capacity'] = data['Capacity'].astype(str)

data.loc[data.a_href == 'https://www.worldfootball.net/venues/mersin-arena-mersin/', 'Capacity'] = '25534'
data.loc[data.a_href == 'https://www.worldfootball.net/venues/stade-paul-lignon-rodez/', 'Capacity'] = '5955'


df2 = data[~data['raw_attendance'].str.contains('\d')]

df2.to_csv('src/Data_processing/missing_capicty.csv')


# print(df2['Capacity'])
# for index, row in data.iterrows():
#     if row['check_raw'] == 'str'
# print(data[['Capacity', 'raw_attendance']])
data[['raw_attendance', 'Capacity']].astype(int)
# print(data[['raw_attendance', 'Capacity']].dtypes)
data['capacity_filled'] = data['raw_attendance']/data['Capacity']

print(data['capacity_filled'])