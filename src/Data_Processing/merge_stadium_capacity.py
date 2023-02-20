import pandas as pd
import pickle

combine_data = pd.read_pickle('data/Data_to_change/betting_and_match_data.pkl')
stadium_data = pd.read_csv('data/RAWDATA/stadium_data.csv')

print(combine_data)
# print(stadium_data)
stadium_data = stadium_data[['stadium', 'City', 'Country', 'Capacity', 'url']]
stadium_data = stadium_data.drop_duplicates(subset='url').reset_index()
print(len(stadium_data['url']))

# print(combine_data[['stadium','attendance']].dtypes)
# print(stadium_data.dtypes)
# # print(len(stadium_data['url'].unique()))
# # print(len(combine_data['a_href'].unique()))
total_df = pd.merge(combine_data, stadium_data, left_on=['a_href'], right_on=['url'], indicator= True)
# # total_df = total_df[total_df['_merge'] != 'right_only']

total_df.to_csv('data/Data_to_change/complete_data.csv')
total_df.to_pickle('data/Data_to_change/complete_data.pkl')
print(total_df)
print(total_df.isna().sum())