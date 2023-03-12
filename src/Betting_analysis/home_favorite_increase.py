import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

bet_data = pd.read_pickle('data/final_datasets/dataset_no_over_capacity.pkl')

h_fav = []

for index, rows in bet_data.iterrows():
    if rows['B365H'] > rows['B365A']:
        h_fav = h_fav + [1]
    else:
        h_fav = h_fav + [0]


        
bet_increase_bool = bet_data
bet_increase_bool['home_favorite'] = h_fav

print(bet_increase_bool)