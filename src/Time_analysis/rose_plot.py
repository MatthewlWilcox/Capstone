import pandas as pd
import plotly.express as px
total_data = pd.read_pickle('data/final_datasets/data_standardized.pkl')


time_df = total_data[[
    'date', 'time', 'day_of_week', 'date_time', 'raw_attendance', 'capacity_filled', 'standard_attend', 'division'
]]
day_categories = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

grouped_week_count_division =  time_df.groupby(['day_of_week', 'division']).count().reset_index()

grouped_week_count_division['day_of_week'] = pd.Categorical(grouped_week_count_division['day_of_week'], categories= day_categories)
grouped_week_count_division.sort_values(by = 'day_of_week', inplace = True)
grouped_week_count_division = grouped_week_count_division[['day_of_week', 'division', 'date']]

print(grouped_week_count_division)
total_div_number = grouped_week_count_division.groupby('day_of_week').sum().reset_index()
# print(total_div_number)
rose_df = pd.merge(grouped_week_count_division, total_div_number, on= 'day_of_week')
rose_df['pct'] = rose_df['date_x']/rose_df['date_y']
# print(rose_df)

fig = px.bar_polar(rose_df, theta = 'day_of_week', r = 'pct', color = 'division')
fig.show()
