import seaborn as sns
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
import july
from datetime import datetime as dt
from jupyter_dash import JupyterDash
from dash import html, dcc, Input, Output
import plotly.graph_objects as go
from datetime import datetime, time
from re import sub
import re
import plotly.express as px
import pickle


model_dataset = pd.read_pickle('data/final_datasets/data_standardized.pkl')
model_dataset = model_dataset.dropna(subset = ['B365A', 'BWH', 'WHH', 'VCD','BbMx>2.5',
                             'BbAv>2.5', 'BbMx<2.5', 'BbAv<2.5', 'std_attend', 'standard_attend'])
model_dataset = model_dataset.drop(['date_time'], axis =1)
obj_data = model_dataset.select_dtypes(include=['object']).copy()
column_obj_name = obj_data.columns.values.tolist()

label_encoder = LabelEncoder()


for obj in column_obj_name:
    model_dataset[obj] = label_encoder.fit_transform(model_dataset[obj])
model_dataset = model_dataset.astype(float)
model_dataset = model_dataset.dropna()


x = model_dataset.drop(['raw_attendance', 'standard_attend'], axis = 1)
x = x[['home_team', 'away_team', 'division', 'date', 'time', 'day_of_week','B365H', 'B365D',
       'B365A']]
y = model_dataset['raw_attendance']

x_train, x_test, y_train, y_test = train_test_split(x,y, test_size = .2, random_state = 11)




rf_model = pickle.load(open('src/Modeling/Random_forest_model.sav', 'rb'))
y_predict = rf_model.predict(x_test)

print(y_test)
model_result = x_test
print(model_result)
model_result['raw_attendance'] = y_test
print(model_result)
model_result['predicted_attend'] = y_predict

print(model_result)


in_fifty = []
in_five_hundred =[]
in_one_thousand =[]
in_fiften_hundreed =[]
for index, rows in model_result.iterrows():
    if rows['predicted_attend'] < rows['raw_attendance']+500 and rows['predicted_attend'] > 500:
        in_five_hundred += [True]
    else:
        in_five_hundred += [False]




model_result['in_five_hundred'] = in_five_hundred

print(model_result)