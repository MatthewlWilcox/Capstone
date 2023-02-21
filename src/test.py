import pandas as pd
import pickle
import numpy as np
data = pd.read_pickle('data/Data_to_change/complete_data.pkl')

data = data[data['year']<= 2019]
print(data)
data2 = data[data['Div'].isnull()]
data2 = data2[data2['Country'] == 'England']

list_na = data['home_team'].to_list()
print(list(set(list_na)))
countries= data['Country'].to_list()
# print(list(set(countries)))
data2.to_csv("src/Data_Processing/null_process/div_null_england_df.csv")
# print(data2)