import pandas as pd
from datetime import datetime as dt
import matplotlib.pyplot as plt
from plotly_calplot import calplot
import july
data = pd.read_pickle('d:/Python Work/Capstone/data/final_datasets/data_standardized.pkl')

data['month_day'] = data['date_time'].dt.strftime('%m-%d')

date_of_year = data.groupby('month_day').mean()
date_of_year['count'] = date_of_year['standard_attend']
date_of_year = date_of_year['count'].sort_values().reset_index()
print(date_of_year)
date_of_year['total_date'] = '2024-' + date_of_year['month_day']
# print(date_of_year['month_day'])
# print(date_of_year['total_date'])

date_of_year['total_date']= pd.to_datetime(date_of_year['total_date'], format = "%Y-%m-%d")

# print(date_of_year)

events = pd.Series(date_of_year['count'].values.tolist(), index = date_of_year['total_date'].values.tolist())
# date_of_year = date_of_year.set_index(pd.DatetimeIndex(date_of_year['total_date']))
# date_of_year = date_of_year['count']
print(date_of_year)
# calplot.yearplot(date_of_year, cmap = 'viridis', monthticks = False)
# plt.show()
july.heatmap(dates = date_of_year['total_date'], data = date_of_year['count'],  cmap='Pastel1', date_label = True, fontsize =10, weekday_label=False, year_label= False, title = 'Avg Attendance per day Standardized 2010-2019', colorbar= True, dpi =1200)
plt.savefig('results/combined_calendar_heatmap_mean.png')
plt.show()
