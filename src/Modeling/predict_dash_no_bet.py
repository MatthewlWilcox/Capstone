from sklearn.ensemble import RandomForestRegressor
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn import metrics
from sklearn.linear_model import LinearRegression
import pickle
from dash import Dash, dash_table, html, dcc, Input, Output
import time

model_dataset = pd.read_pickle('data/final_datasets/data_standardized.pkl')
print(model_dataset)
model_dataset = model_dataset.dropna(subset = ['B365A', 'BWH', 'WHH', 'VCD','BbMx>2.5',
                             'BbAv>2.5', 'BbMx<2.5', 'BbAv<2.5', 'std_attend', 'standard_attend'])
model_dataset = model_dataset.drop(['date_time'], axis =1)
obj_data = model_dataset.select_dtypes(include=['object']).copy()
column_obj_name = obj_data.columns.values.tolist()
before_encode = model_dataset[['division', 'home_team', 'away_team', 'date', 'time']]

label_encoder = LabelEncoder()

pickle.dump(label_encoder, open('src/Modeling/label_encoder.sav', 'wb'))


for obj in column_obj_name:
    model_dataset[obj] = label_encoder.fit_transform(model_dataset[obj])
model_dataset = model_dataset.astype(float)
model_dataset = model_dataset.dropna()

post_encode = model_dataset[['division', 'home_team', 'away_team','date', 'time']]

encode_compare = pd.concat([before_encode, post_encode], axis = 1, ignore_index=True)
encode_compare.columns = ['division', 'home_team', 'away_team', 'date', 'time', 'division_encode', 'home_encode', 'away_encode', 'date_encode', 'time_encode']
# print(encode_compare)

div_key = pd.Series(encode_compare.division.values, index = encode_compare.division_encode).to_dict()
home_key = pd.Series(encode_compare.home_team.values, index = encode_compare.home_encode).to_dict()
away_key = pd.Series(encode_compare.away_team.values, index = encode_compare.away_encode).to_dict()
date_key = pd.Series(encode_compare.date.values, index = encode_compare.date_encode).to_dict()
time_key = pd.Series(encode_compare.time.values, index = encode_compare.time_encode).to_dict()





x = model_dataset.drop(['raw_attendance', 'standard_attend'], axis = 1)
x = x[['home_team', 'away_team', 'division', 'date', 'time', 'day_of_week']]
y = model_dataset['raw_attendance']

x_train, x_test, y_train, y_test = train_test_split(x,y, test_size = .2, random_state = 11)


random_forest_model = pickle.load(open('src/Modeling/Random_forest_model_no_bet.sav', 'rb'))


y_predict = random_forest_model.predict(x_test)

mae = metrics.mean_absolute_error(y_test, y_predict)
mse = metrics.mean_squared_error(y_test, y_predict)
mape = metrics.mean_absolute_percentage_error(y_test, y_predict)
r2 = metrics.r2_score(y_test, y_predict)
result_df = pd.DataFrame(np.array([['Mean Absolute Error', mae], ['Mean Squared Error', mse],
    ['Mean Absolute Percentage Error', mape], ['r\u00b2', r2]]), columns = ['Metric', 'Score'])
print(result_df)