import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt



time_df = pd.read_pickle('d:/Python Work/Capstone/data/final_datasets/time_shrink.pkl')

df_grouped_median_tod= time_df.groupby(time_df['date_time'].dt.hour).median()



df_grouped_count = time_df.groupby(time_df['date_time'].dt.hour).count()
print(df_grouped_count)
df_grouped_count = df_grouped_count['raw_attendance'].reset_index()
df_grouped_count['count'] = df_grouped_count['raw_attendance']
df_grouped_count = df_grouped_count[['date_time', 'count']]
# df_grouped_count= df_grouped_count.rename(columns = {'date':'count'})
print(df_grouped_count)

df_count_atted = pd.merge(df_grouped_count, df_grouped_median_tod, on = 'date_time')
df_count_atted = df_count_atted.drop(columns= ['capacity_filled'])
df_count_atted.rename( columns = {'raw_attendance': 'Attendance', 'count': "Number of Games"}, inplace= True)
print(df_count_atted)
melted_count_attend = pd.melt(df_count_atted, value_vars=['Number of Games', 'Attendance'], id_vars= 'date_time')
print(melted_count_attend)

sns.lineplot(data = melted_count_attend, x = 'date_time', y = 'value', hue = 'variable')
plt.title('Attendance and Game Count by Time of Day')
plt.xlabel('Hour of the Day')
# sns.lineplot(data = )
# melt_df_grouped = 
# sns.lineplot(data = df_grouped_count, x = 'date_time', y = 'raw_attendance', markers = True, marker = "o" )
# sns.lineplot(data = df_grouped_median_tod, x = 'date_time', y = 'raw_attendance', markers = True, marker = "o" )


plt.show()