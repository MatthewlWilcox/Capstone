import pandas as pd
data = pd.read_pickle('data/Data_to_change/complete_data.pkl')

data = data[data['year']<= 2019]
data.to_pickle('data/Data_to_change/complete_data_before_2019.pkl')
data.to_csv('data/Data_to_change/complete_data_before_2019.csv')