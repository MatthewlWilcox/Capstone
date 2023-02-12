import pandas as pd


df = pd.read_pickle('data/RAWDATA/match_data.pkl')



df.to_csv('data/RAWDATA/RAW_match_data.csv')

print(df)