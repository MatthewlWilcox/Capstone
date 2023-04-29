import pandas as pd
import pickle
from datetime import datetime, time
from re import sub
from datetime import datetime as dt
import re
betting_data = pd.read_csv('data/RAWDATA/RAW_betting_data.csv')
match_data =  pd.read_csv('data/RAWDATA/RAW_match_data.csv')
with open('src/Data_Processing/key_dictionary.pkl', 'rb') as pick:
    key_dict = pickle.load(pick)
def snake_case(s):
  return '_'.join(
    sub('([A-Z][a-z]+)', r' \1',
    sub('([A-Z]+)', r' \1',
    s.replace('-', ' '))).split()).lower()
betting_data['HomeTeam'] =betting_data['HomeTeam'].apply(str)
betting_data['HomeTeam'] =betting_data['HomeTeam'].apply(snake_case)
betting_data['AwayTeam'] =betting_data['AwayTeam'].apply(str)
betting_data['AwayTeam'] =betting_data['AwayTeam'].apply(snake_case)

betting_data['HomeTeam'] = betting_data['HomeTeam'].replace(key_dict)
betting_data['AwayTeam'] = betting_data['AwayTeam'].replace(key_dict)

match_data['home_team'] =match_data['home_team'].apply(str)
match_data['home_team'] =match_data['home_team'].apply(snake_case)
match_data['away_team'] =match_data['away_team'].apply(str)
match_data['away_team'] =match_data['away_team'].apply(snake_case)

match_data['Hohome_teammeTeam'] = match_data['home_team'].replace(key_dict)
match_data['away_team'] = match_data['away_team'].replace(key_dict)

# betting_data.to_pickle('data/Data_to_change/betting_data_updated_names.pkl')
# match_data.to_pickle('data/Data_to_change/match_data_updated_names.pkl')


# match_data = pd.read_pickle('data/Data_to_change/match_data_updated_names.pkl')
# betting_data = pd.read_pickle('data/Data_to_change/betting_data_updated_names.pkl')
# print(match_data)

month_key = {'August': '8', 'September':'9', 'October':'10', 'November': '11','December':'12', 'January':'1', 'February':'2', 'March':'3', 'April':'4', 'May':'5', 'June' : '6', 'July':'7'}

match_data['month']= match_data['month'].replace(month_key)

match_data['date'] = match_data['day_of_month'].astype(str) + "-" + match_data['month'].astype(str) + "-" + match_data['year'].astype(str)

match_data['date'] = pd.to_datetime(match_data['date'])
betting_data['Date'] = pd.to_datetime(betting_data['Date'])
# print(betting_data)
# print(match_data)
# print(betting_data.dtypes)
# print(match_data.dtypes)

# # match_data.to_pickle('data/Data_to_change/match_data_updated_date.pkl')
# # betting_data.to_pickle('data/Data_to_change/betting_data_updated_date.pkl')


# # match_data = pd.read_pickle('data/Data_to_change/match_data_updated_date.pkl')
# # betting_data = pd.read_pickle('data/Data_to_change/betting_data_updated_date.pkl')
# print(match_data)
# print(betting_data)


merged_df = pd.merge(match_data, betting_data, left_on = ['date', 'home_team', 'away_team'], right_on = ['Date', 'HomeTeam', 'AwayTeam'], how ='left', indicator=False)

# print(merged_df)


# merged_df.to_pickle('data/Data_to_change/betting_and_match_data.pkl')
# merged_df.to_csv('data/Data_to_change/betting_and_match_data.csv')

# data = pd.read_pickle('data/Data_to_change/complete_data.pkl')
data = merged_df
data = data[data['year']<= 2019]
# data.to_pickle('data/Data_to_change/complete_data_before_2019.pkl')
# data.to_csv('data/Data_to_change/complete_data_before_2019.csv')


# data = pd.read_pickle('data/Data_to_change/complete_data_before_2019.pkl')


data = data[['home_team','away_team','home_score','away_score','date','time','day_of_week','attendance','Div','FTHG','FTAG','FTR','HTHG','HTAG','HTR','B365H','B365D','B365A','BWH','BWD','BWA','WHH','WHD','WHA','VCH','VCD','VCA','BbMx>2.5','BbAv>2.5','BbMx<2.5','BbAv<2.5']]

# print(data)


# data.to_pickle("data/Data_to_change/complete_data_2010_2019_shrunk.pkl")
# data.to_csv("data/Data_to_change/complete_data_2010_2019_shrunk.csv")

# data = pd.read_pickle('data/Data_to_change/complete_data_2010_2019_shrunk.pkl')

# for col in data.columns:
    # print(col)

data = data.rename(columns = {'attendance':'raw_attendance'})
# data['Capacity'] = data['Capacity'].astype(str)

# data.loc[data.url == 'https://www.worldfootball.net/venues/mersin-arena-mersin/', 'Capacity'] = '25534'
# data.loc[data.url == 'https://www.worldfootball.net/venues/stade-paul-lignon-rodez/', 'Capacity'] = '5955'


# df2 = data[data['away_score'].str.contains('\d')]
# print(df2)
# df2.to_csv('src/Data_processing/missing_capicty.csv')

data = data[data['raw_attendance'].str.contains('\d')]
data['raw_attendance'] = data['raw_attendance'].astype(float)
# data['Capacity'] = data['Capacity'].astype(float)

def remove_non_numberics(s):
    return sub('[^0-9]', '', s)

data['away_score'] = data['away_score'].apply(lambda x: re.sub('[^0-9]', '', x))

# print(df2['Capacity'])
# for index, row in data.iterrows():
#     if row['check_raw'] == 'str'
# print(data[['Capacity', 'raw_attendance']])


# print(data[['raw_attendance', 'Capacity']].dtypes)
# data['capacity_filled'] = data['raw_attendance']/data['Capacity']
# data['capacity_filled'] = data['capacity_filled'].round(4)


# Alter Data types:
data= data.rename(columns={ 'Div':'division'})
data['home_score']= data['home_score'].astype(int)
data['away_score'] = data['away_score'].astype(int)
data['date'] = data['date'].astype(str)
# data['time'] = data['time'].apply(lambda x: datetime.strptime(x, '%H:%M'))
data['date_time'] = data.apply(lambda row: pd.to_datetime(str(row['date']) + ' ' + str(row['time'])),axis = 1)
data['raw_attendance']= data['raw_attendance'].astype(int)
print(data)

# data.to_pickle('data/final_datasets/Total_data.pkl')

# data.to_csv('data/final_datasets/Total_data.csv')

# data = pd.read_pickle('data/final_datasets/Total_data.pkl')

season = []
for index, rows in data.iterrows():
    match_day = dt.strptime(rows['date'], '%Y-%m-%d')
    # print(match_day)
    year = int(dt.strftime(match_day, '%Y'))
    month_day = dt.strftime(match_day, '%m-%d')
    # print(int(year))
    # print(type(year))
    # print(month_day)
    cutoff_date = dt.strftime(dt(2014,7,14), '%m-%d')
    if month_day > cutoff_date:
        year = year +1
        season = season + [year]

    else:
        season = season + [year]

# def stand_dev(x): return np.std(x)

data['season'] = season

data_std = data.groupby(['home_team', 'season'])['raw_attendance'].std().reset_index()
# print(data_std)
data_std = data_std.rename(columns = {'raw_attendance':'std_attend'})
# print(data_std[data_std['std_attend'].isna()])
data_mean = data.groupby(['home_team', 'season']).mean().reset_index()
data_mean = data_mean[['home_team', 'season', 'raw_attendance']].rename(columns = {'raw_attendance': 'mean_attend'})
data = pd.merge(data, data_mean, on = ['home_team', 'season'])
data = pd.merge(data, data_std, on= ['home_team', 'season'])
data['standard_attend'] = (data['raw_attendance']-data['mean_attend'])/ data['std_attend']
# data.to_pickle('data/final_datasets/data_standardized.pkl')
# data.to_csv('data/final_datasets/data_standardized.csv')