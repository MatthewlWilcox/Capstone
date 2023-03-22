import pandas as pd

data = pd.read_csv('data/Data_to_change/complete_data.csv')
# print(data['Div'].value_counts())
data2 = pd.read_csv('data/final_datasets/data_standardized.csv')
data2 = data2[data2['division']!= 'SC2']
data2 = data2[['home_team', 'away_team', 'raw_attendance', 'stadium', 'city', 'country', 
              'division', 'FTHG', 'FTAG', 'FTR', 'HTHG', 'HTAG', 'HTR',
              'B365H', 'B365D', 'B365A', 'BWH', 'BWD', 'BWA' ,'WHH', 'WHD', 'WHA', 
              'VCH', 'VCD', 'VCA', 'BbMx>2.5', 'BbAv>2.5', 'BbMx<2.5', 'BbAv<2.5', 'date_time',
              'season', 'mean_attend', 'std_attend', 'standard_attend']]
print(data2.isna().sum()*100/len(data2))