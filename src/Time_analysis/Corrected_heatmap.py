import pandas as pd
from datetime import datetime as dt

from plotly_calplot import calplot

data = pd.read_pickle('data/final_datasets/Total_data.pkl')

data['month_day'] = data['date_time'].dt.strftime('%m-%d')

date_of_year = data.groupby('month_day').count()
date_of_year['count'] = date_of_year['home_team']
date_of_year = date_of_year['count'].sort_values().reset_index()
date_of_year['month_day'] = '2024-' +date_of_year['month_day']
print(date_of_year)

date_of_year['month_day'] = pd.to_datetime(date_of_year['month_day'], format="%Y-%m-%d")
# date_of_year['month_day'] = date_of_year['month_day'].apply(lambda x: x.replace(year = 2024))
print(date_of_year)

fig = calplot(date_of_year, x = 'month_day', y = 'count')
fig.show()