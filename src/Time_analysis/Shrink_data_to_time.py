import pandas as pd

df = pd.read_pickle('data/final_datasets/data_standardized.pkl')

print(df.columns)

time_df = df[[
    'date', 'time', 'day_of_week', 'date_time', 'raw_attendance', 'capacity_filled', 'standard_attend'
]]
time_df.to_pickle('data/final_datasets/time_shrink.pkl')
time_df.to_csv('data/final_datasets/time_shrink.csv')