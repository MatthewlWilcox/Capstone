import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

bet_data = pd.read_pickle('data/final_datasets/dataset_no_over_capacity.pkl')
print(bet_data.columns)
bet_data =bet_data.sort_values('capacity_filled', ascending = False)

print(bet_data)
bet_data2 = bet_data[['home_team', 'raw_attendance', 'capacity_filled', 'capacity', 'division', 'B365H', 'B365D', 'B365A', 'avg_attendance', 'std_attendance']]
bet_dif = bet_data2
bet_dif['dif'] = bet_dif['B365H']-bet_dif['B365A']
bet_dif['abs_dif'] = abs(bet_dif['B365H']-bet_dif['B365A'])
# grouped_bet_dif_mean = bet_dif.groupby(['division', 'home_team']).mean().reset_index()
# print(grouped_bet_dif_mean)
# grouped_bet_dif_mean = grouped_bet_dif_mean[['division', 'home_team', 'raw_attendance']].rename(columns = {'raw_attendance': 'avg_attendance'})
# grouped_bet_dif_std = bet_dif.groupby(['division', 'home_team']).std().reset_index()
# print(grouped_bet_dif_mean)
# grouped_bet_dif_std = grouped_bet_dif_std[['division', 'home_team', 'raw_attendance']].rename(columns = {'raw_attendance': 'std_attendance'})

# bet_dif = pd.merge(bet_dif, grouped_bet_dif_mean, on = ['division', 'home_team'])
# bet_dif = pd.merge(bet_dif, grouped_bet_dif_std, on = ['division', 'home_team'])
bet_dif['zscore'] = (bet_dif['raw_attendance'] - bet_dif['avg_attendance'])/bet_dif['std_attendance']
print(bet_dif)

bet_dif = bet_dif[(bet_dif['zscore']<3) & (bet_dif['zscore'] > -3)]
sns.lmplot(data = bet_dif, y = 'zscore', x ='dif')
plt.show()




sns.scatterplot(data = bet_dif, y = 'zscore', x ='abs_dif')
plt.show()
bet_dif=bet_dif[['capacity_filled', 'dif']]
print(bet_dif)


bet_dif_pivot = bet_dif.pivot(columns = ['capacity_filled', 'dif'])
print(bet_dif_pivot)
sns.histplot(data = bet_dif, x = 'capacity_filled')
plt.show()
sns.scatterplot(data = bet_dif, x = 'dif', y = 'capacity_filled')
plt.show()

sns.heatmap(data = bet_dif_pivot)
plt.show()