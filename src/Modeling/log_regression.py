from sklearn.ensemble import RandomForestRegressor
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn import metrics
from sklearn.linear_model import LinearRegression, LogisticRegression
data = pd.read_pickle('data/final_datasets/data_standardized.pkl')

data = data[data['division'].isin(['E0', 'D1','I1', 'SP1', 'F1'])]
data = data.dropna(subset = ['B365A', 'BWH', 'WHH', 'VCD','BbMx>2.5',
                             'BbAv>2.5', 'BbMx<2.5', 'BbAv<2.5', 'std_attend', 'standard_attend'])
data = data.drop(['url', 'date_time'], axis =1)
obj_data = data.select_dtypes(include=['object']).copy()
column_obj_name = obj_data.columns.values.tolist()
print(1)
dummy_list = []

for index, rows in data.iterrows():
    if rows['standard_attend'] > 0:
        dummy_list = dummy_list + [1]
    else:
        dummy_list = dummy_list + [0]



label_encoder = LabelEncoder()


for obj in column_obj_name:
    data[obj] = label_encoder.fit_transform(data[obj])
data = data.astype(float)
data = data.dropna()

x = data.drop(['raw_attendance', 'standard_attend', 'capacity_filled'], axis = 1)
x = x[['home_team', 'away_team', 'division', 'date', 'time', 'day_of_week','B365H', 'B365D',
       'B365A']]
y = data['raw_attendance']

print(2)


log_model = LogisticRegression(random_state= 42069)

log_model.fit(x,y)

print(log_model.score(x,y))