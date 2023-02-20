import pandas as pd
import pickle

combine_data = pd.read_pickle('data/Data_to_change/betting_and_match_data.pkl')
stadium_data = pd.read_pickle('data/RAWDATA/stadium_data.pkl')

total_df = pd.merge(combine_data, stadium_data, left_on=['a_href'], right_on=['url'])

total_df.to_csv('data/Data_to_change/complete_data.csv')

print(total_df)