import pandas as pd
import pickle 
from datetime import datetime
match_data = pd.read_pickle('data/Data_to_change/match_data_updated_names.pkl')
betting_data = pd.read_pickle('data/Data_to_change/betting_data_updated_names.pkl')
# print(match_data)

month_key = {'August': '8', 'September':'9', 'October':'10', 'November': '11','December':'12', 'January':'1', 'February':'2', 'March':'3', 'April':'4', 'May':'5', 'June' : '6', 'July':'7'}

match_data['month']= match_data['month'].replace(month_key)

match_data['date'] = match_data['day_of_month'].astype(str) + "-" + match_data['month'].astype(str) + "-" + match_data['year'].astype(str)

match_data['date'] = pd.to_datetime(match_data['date'])
betting_data['Date'] = pd.to_datetime(betting_data['Date'])
print(betting_data)
print(match_data)
print(betting_data.dtypes)
print(match_data.dtypes)

match_data.to_pickle('data/Data_to_change/match_data_updated_date.pkl')
betting_data.to_pickle('data/Data_to_change/betting_data_updated_date.pkl')