import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

bet_data = pd.read_pickle('data/final_datasets/data_standardized.pkl')
bet_data = bet_data.dropna(subset = ['B365H', 'B365A'])
h_fav = []
attend_increase = []
for index, rows in bet_data.iterrows():
    if rows['B365H'] > rows['B365A']:
        h_fav = h_fav + [1]
    else:
        h_fav = h_fav + [0]
    if rows['standard_attend'] >= 0:
        attend_increase = attend_increase + [1]
    else:
        attend_increase = attend_increase + [0]
print(h_fav)
        
bet_increase_bool = bet_data
bet_increase_bool['home_fav'] = h_fav
bet_increase_bool['attend_increase'] = attend_increase
bet_bool = bet_increase_bool[['home_fav', 'attend_increase','raw_attendance']]
bet_bool = bet_bool.groupby(['home_fav', 'attend_increase']).count().reset_index()
bet_bool = bet_bool.pivot_table(values = 'raw_attendance', index = 'home_fav', columns = 'attend_increase')
print(bet_bool)

sns.heatmap(bet_bool)
plt.show()





