import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



data = pd.read_pickle('data/final_datasets/time_shrink.pkl')
data['month'] = data.date_time.dt.month
data['day'] = data.date_time.dt.day
df_grouped = data.groupby([data['month'], data['day']]).mean().reset_index()
# df_grouped = df_grouped.rename(columns = {'date'})
# df_grouped['date'] = data['month'].astype(str) +  data['day'].astype(str)
# # df_grouped = df_grouped.drop(columns =['month', 'day'])
# df_grouped['date'] = pd.to_datetime(df_grouped['date'], format='%m%d')
print(df_grouped)
# print(reset)

result_mean_attenance = df_grouped.pivot(index= 'month', columns = 'day', values ='raw_attendance')

sns.heatmap(result_mean_attenance)
# plt.show()
plt.savefig('results/Question 3/heatmap.png',dpi=1200)


