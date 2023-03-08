import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt



time_df = pd.read_pickle('d:/Python Work/Capstone/data/final_datasets/time_shrink.pkl')

df_grouped_median_tod= time_df.groupby(time_df['date_time'].dt.hour).median()



df_grouped_count = time_df.groupby(time_df['date_time'].dt.hour).count()
df_grouped_count = df_grouped_count['raw_attendance'].reset_index()
# df_grouped_count= df_grouped_count.rename(columns = {'date':'count'})
print(df_grouped_count)
# sns.lineplot(data = df_grouped_median_tod, x = 'date_time', y = 'raw_attendance', markers = True, marker = "o" )
# ax2 = plt.twinx()
sns.lineplot(data = df_grouped_count, x = 'date_time', y = 'raw_attendance', markers = True, marker = "o" )
sns.lineplot(data = df_grouped_median_tod, x = 'date_time', y = 'raw_attendance', markers = True, marker = "o" )


plt.show()