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

before_encode = model_dataset[['division', 'home_team', 'away_team']]

for obj in column_obj_name:
    model_dataset[obj] = label_encoder.fit_transform(model_dataset[obj])

post_encode = model_dataset[['division', 'home_team', 'away_team']]

encode_compare = pd.concat([before_encode, post_encode], axis = 1, ignore_index=True)
encode_compare.columns = ['division', 'home_team', 'away_team', 'division_encode', 'home_encode', 'away_encode']
# print(encode_compare)

div_key = pd.Series(encode_compare.division.values, index = encode_compare.division_encode).to_dict()
home_key = pd.Series(encode_compare.home_team.values, index = encode_compare.home_encode).to_dict()
away_key = pd.Series(encode_compare.away_team.values, index = encode_compare.away_encode).to_dict()


# print(model_dataset.dtypes)
model_dataset = model_dataset.astype(float)
model_dataset = model_dataset.dropna()

x = model_dataset.drop(['raw_attendance', 'standard_attend'], axis = 1)
x = x[['home_team', 'away_team', 'division', 'date', 'time', 'day_of_week','B365H', 'B365D',
       'B365A']]
y = model_dataset['raw_attendance']

x_train, x_test, y_train, y_test = train_test_split(x,y, test_size = .2, random_state = 11)




rf_model = pickle.load(open('src/Modeling/Random_forest_model.sav', 'rb'))
y_predict = rf_model.predict(x_test)

# print(y_test)
model_result = x_test
# print(model_result)
model_result['raw_attendance'] = y_test
# print(model_result)
model_result['predicted_attend'] = y_predict
model_result['division'] = model_result['division'].astype(int)
model_result['home_team'] = model_result['home_team'].astype(int)
model_result['away_team'] = model_result['away_team'].astype(int)
print(div_key)
model_result = model_result.replace({'division':div_key, 'home_team': home_key, 'away_team':away_key})
print(model_result)


in_50 = []
in_500 =[]
in_750 =[]
in_1000 =[]
in_1500 =[]

for index, rows in model_result.iterrows():
    if rows['predicted_attend'] < rows['raw_attendance']+50 and rows['predicted_attend'] > rows['raw_attendance']-50:
        in_50 += [True]
    else:
        in_50 += [False]
    if rows['predicted_attend'] < rows['raw_attendance']+500 and rows['predicted_attend'] > rows['raw_attendance']-500:
        in_500 += [True]
    else:
        in_500 += [False]
    if rows['predicted_attend'] < rows['raw_attendance']+750 and rows['predicted_attend'] > rows['raw_attendance']-750:
        in_750 += [True]
    else:
        in_750 += [False] 

    if rows['predicted_attend'] < rows['raw_attendance']+1000 and rows['predicted_attend'] > rows['raw_attendance']-1000:
        in_1000 += [True]
    else:
        in_1000 += [False] 
    if rows['predicted_attend'] < rows['raw_attendance']+1500 and rows['predicted_attend'] > rows['raw_attendance']-15000:
        in_1500 += [True]
    else:
        in_1500 += [False] 



model_result['in_50'] = in_50
in_50_grouped = model_result.groupby('in_50').count()['date'].reset_index()
in_50_grouped['pct'] = in_50_grouped['date']/sum(in_50_grouped['date'])
in_50_grouped_div = model_result.groupby(['in_50', 'division']).count()['date'].reset_index()
in_50_grouped_div['pct'] = in_50_grouped_div['date']/sum(in_50_grouped_div['date'])


model_result['in_500'] = in_500
in_500_grouped = model_result.groupby('in_500').count()['date'].reset_index()
in_500_grouped['pct'] = in_500_grouped['date']/sum(in_500_grouped['date'])
in_500_grouped_div = model_result.groupby(['in_500', 'division']).count()['date'].reset_index()
in_500_grouped_div['pct'] = in_500_grouped_div['date']/sum(in_500_grouped_div['date'])

model_result['in_750'] = in_750
in_750_grouped = model_result.groupby('in_750').count()['date'].reset_index()
in_750_grouped['pct'] = in_750_grouped['date']/sum(in_750_grouped['date'])
in_750_grouped_div = model_result.groupby(['in_750', 'division']).count()['date'].reset_index()
in_750_grouped_div['pct'] = in_750_grouped_div['date']/sum(in_750_grouped_div['date'])

model_result['in_1000'] = in_1000
in_1000_grouped = model_result.groupby('in_1000').count()['date'].reset_index()
in_1000_grouped['pct'] = in_1000_grouped['date']/sum(in_1000_grouped['date'])
in_1000_grouped_div = model_result.groupby(['in_1000', 'division']).count()['date'].reset_index()
in_1000_grouped_div['pct'] = in_1000_grouped_div['date']/sum(in_1000_grouped_div['date'])

model_result['in_1500'] = in_1500
in_1500_grouped = model_result.groupby('in_1500').count()['date'].reset_index()
in_1500_grouped['pct'] = in_1500_grouped['date']/sum(in_1500_grouped['date'])
in_1500_grouped_div = model_result.groupby(['in_1500', 'division']).count()['date'].reset_index()
in_1500_grouped_div['pct'] = in_1500_grouped_div['date']/sum(in_1500_grouped_div['date'])


# print(model_result)

# print(in_50_grouped)
print(in_50_grouped)



import plotly.graph_objects as go


fig = go.Figure()

fig.add_trace(
    go.Pie(labels = in_50_grouped['in_50'], values= in_50_grouped['pct'], name = '50')
)
fig.add_trace(
    go.Pie(labels = in_500_grouped['in_500'], values = in_500_grouped['pct'], name = "500")
)
fig.add_trace(
    go.Pie(labels= in_750_grouped['in_750'], values= in_750_grouped['pct'], name = '750')
)
fig.add_trace(
    go.Pie(labels = in_1000_grouped['in_1000'], values = in_1000_grouped['pct'], name = '1000')
)
fig.add_trace(
    go.Pie(labels = in_1500_grouped['in_5000'], values = in_1500_grouped['pct'], name= '1500')
)

fig.update_layout(
    updatemenus=[
        dict(
            active=0,
            buttons=list([
                dict(label="50",
                     method="update",
                     args=[{"visible": [True, False, True, False]},
                           {"title": "Within 50"}]),
                dict(label="500",
                     method="update",
                     args=[{"visible": [True, True, False, False]},
                           {"title": "Witnhin 500"}
                            ]),
                dict(label="750",
                     method="update",
                     args=[{"visible": [False, False, True, True]},
                           {"title": "Within 750"}]),
                dict(label="1000",
                     method="update",
                     args=[{"visible": [True, True, True, True]},
                           {"title": "Within 1000"}]),
                dict(label="1500",
                     method="update",
                     args=[{"visible": [True, True, True, True]},
                           {"title": "Within 1500"}]), 
            ]),
        )
    ])

fig.update_layout(title_text="Yahoo")

fig.show()