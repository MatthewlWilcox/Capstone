import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
data = pd.read_pickle('data/final_datasets/time_shrink.pkl' )

print(data.dtypes)

df_grouped_mean= data.groupby(data['date_time'].dt.hour).mean()
df_grouped_median= data.groupby(data['date_time'].dt.hour).median()


fig, ax = plt.subplots(figsize=(15, 10))
fig1 = sns.lineplot(df_grouped_mean, x = 'date_time', y = 'raw_attendance', ax = ax, markers = True, marker = "o" )
fig1.set(title = "Mean Raw Attendance by time of the day", xlabel ='Hour of the Day', ylabel = 'Raw Attendance')


# plt.show()
fig1.show()


fig, ax = plt.subplots(figsize=(15, 10))
fig2 = sns.lineplot(df_grouped_mean, x = 'date_time', y = 'capacity_filled', ax=ax,  markers = True, marker = "o" )
fig2.set(title = "Mean Capacity Filled by time of the day", xlabel ='Hour of the Day', ylabel = 'Capacity Filled')

# plt.show()
fig2.figure.savefig('results/Question 2/mean_capacity_filled_time_day.png',dpi=1200)


fig, ax = plt.subplots(figsize=(15, 10))
fig3 = sns.lineplot(df_grouped_median, x = 'date_time', y = 'raw_attendance', ax = ax,  markers = True, marker = "o" )
fig3.set(title = "Median Raw Attendance by time of the day", xlabel ='Hour of the Day', ylabel = 'Raw Attendance')

# plt.show()
fig3.figure.savefig('results/Question 2/median_raw_attendance_time_day.png',dpi=1200)


fig, ax = plt.subplots(figsize=(15, 10))
fig4 = sns.lineplot(df_grouped_median, x = 'date_time', y = 'capacity_filled', ax=ax,  markers = True, marker = "o" )
fig4.set(title = "Median Capacity Filled by time of the day", xlabel ='Hour of the Day', ylabel = 'Capacity Filled')

# plt.show()
fig4.figure.savefig('results/Question 2/median_capacity_filled_time_day.png',dpi=1200)