import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
import calmap

data = pd.read_pickle('data/final_datasets/time_shrink.pkl')
# print(data)
data['month'] = data.date_time.dt.month
data['day'] = data.date_time.dt.day
# print(data)
# start_date = pd.to_datetime('2015-01-01')
# end_date = pd.to_datetime('2015-12-31')
# data = data.loc[(data['date_time']>= start_date) & (data['date_time']<=end_date)]
df = data[['date_time', 'raw_attendance', 'capacity_filled']]
df['date_time'] = df['date_time'].dt.date
# print(df)
df_grouped = df.groupby('date_time').median().reset_index().sort_values('date_time')
df_grouped['date_time'] = pd.to_datetime(df_grouped['date_time'])
df_grouped['day'] = df_grouped['date_time'].dt.day
df_grouped['month'] = df_grouped['date_time'].dt.month
df_grouped['year'] = df_grouped['date_time'].dt.year


print(df_grouped)
df_grouped.to_csv('src/Time_analysis/calanedar_heat.csv')
# fig = px.density_heatmap(df_grouped, x ='month', y = 'day', z = 'raw_attendance', animation_frame= 'year')
# fig["layout"].pop("updatemenus") 
# fig.show()
# data['month'] = data.date_time.dt.month
# data['day'] = data.date_time.dt.day
# # df_grouped = data.groupby([data['month'], data['day']]).mean().reset_index()
# # # df_grouped = df_grouped.rename(columns = {'date'})
# # df_grouped['date'] = data['month'].astype(str) +  data['day'].astype(str)
# # df_grouped = df_grouped.drop(columns =['month', 'day'])
# # df_grouped['date'] = pd.to_datetime(df_grouped['date'], format='%m%d')
# # print(df_grouped)
# data['date_time'] = pd.to_datetime(data['date_time'])
# start_date = pd.to_datetime('2015-1-1')

# data.set_index('date_time', inplace = True)

# # # print(event_means)

# # result_mean_attenance = df_grouped.pivot(index= 'month', columns = 'day', values ='raw_attendance')

# # sns.heatmap(result_mean_attenance)
# # # plt.show()
# # plt.savefig('results/Question 3/heatmap.png',dpi=1200)


# # fig, ax = calmap.calendarplot(data['raw_attendance'], how = 'mean', monthticks=1, daylabels='MTWTFSS', cmap='YlGn')
# calmap.yearplot(data['raw_attendance'],year = 2015, dayticks= True)
# plt.title('Calendar Plot of Mean Events')
# plt.show()