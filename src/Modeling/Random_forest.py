from sklearn.ensemble import RandomForestRegressor
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import LabelEncoder



data = pd.read_pickle('data/final_datasets/data_standardized.pkl')
data = data.dropna(subset = ['B365A', 'BWH', 'WHH', 'VCD'])
print(data.isna().sum())

std_na_csv = data[data['standard_attend'].isna()]
std_na_csv.to_csv('Test_find_stand_attend_na.csv')
print()
# print(data.columns)
# le = LabelEncoder()
