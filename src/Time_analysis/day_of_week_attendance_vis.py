import pandas as pd
import matplotlib as plt
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_pickle('data/final_datasets/time_shrink.pkl')

df_grouped_mean = df.groupby('day_of_week')['raw_attendance', 'capacity_filled'].mean().reset_index()
df_grouped_median = df.groupby('day_of_week')['raw_attendance', 'capacity_filled'].median().reset_index()

day_categories = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
df_grouped_mean['day_of_week'] = pd.Categorical(df_grouped_mean['day_of_week'], categories= day_categories)
df_grouped_mean.sort_values(by = 'day_of_week', inplace = True)
df_grouped_median['day_of_week'] = pd.Categorical(df_grouped_median['day_of_week'], categories= day_categories)
df_grouped_median.sort_values(by = 'day_of_week', inplace = True)
fig, axs = plt.subplots(ncols=2, sharey=True)
fig.suptitle('Capacity Filled for Day of the Week')
sns.barplot(ax =axs[0],data=df_grouped_mean, x = 'day_of_week', y = 'capacity_filled').set(title ='Mean')
plt.xticks(rotation=90)
sns.barplot(ax =axs[1],data=df_grouped_median, x = 'day_of_week', y = 'capacity_filled').set(title ='Median')
plt.xticks(rotation=90)
plt.savefig('results/Question 1/day_of_week_capacity_filled.png')
fig, axs = plt.subplots(ncols=2, sharey=True,)
fig.suptitle('Raw Attendance for Day of the Week')
sns.barplot(ax =axs[0],data=df_grouped_mean, x = 'day_of_week', y = 'raw_attendance').set(title ='Mean')
plt.xticks(rotation=90)

sns.barplot(ax =axs[1],data=df_grouped_median, x = 'day_of_week', y = 'raw_attendance').set(title ='Median')
plt.xticks(rotation=90)
plt.savefig('results/Question 1/day_of_week_raw_attendance.png')
