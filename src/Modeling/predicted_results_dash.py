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

div_dict = {'D1':'Bundesliga', 'D2': '2. Bundesliga', 'E0':'Premier League', 'E1':'Championship', 
            'E2':'League 1', 'E3':'League 2','SP1':'La Liga Primera', 'SP2':'La Liga Segunda',
              'B1':'Jupiler League', 'F1':'Ligue 1','F2':'Ligue 2','I1':'Serie A','I2':'Serie B', 
              'SC0':'Scottish Premier League', 'SC1':'Scottish Division 1', 'T1':'Fubol Ligi 1', 'P1': 'Liga 1'}
predicted_data = pd.read_pickle('d:/Python Projects/Capstone/src/Modeling/predicted_result_df.pkl')
predicted_data = predicted_data.replace({'division':div_dict})
predicted_data['home_team'] = predicted_data['home_team'].str.replace('_', ' ').apply(lambda x: x.title())
predicted_data['away_team'] = predicted_data['away_team'].str.replace('_', ' ').apply(lambda x: x.title())


predicted_data = predicted_data[['home_team', 'away_team', 'division', 'date', 'time', 'predicted_attend', 'raw_attendance']]


predicted_data.columns =  ['Home Team', 'Away Team', 'League', 'Date of Match', 'Time of Match', 'Predicted Attendance', 'Actual Attendance']
print(predicted_data)


# Load the existing dataframe

# Define the app
app = Dash(__name__)

# Define the layout
app.layout = html.Div([
    dcc.Interval(id='interval-component', interval=10*1000, n_intervals=0),
    html.Table(id='table', style={'border': '1px solid black'}),
])

# Define the callback to update the table
@app.callback(Output('table', 'children'),
              [Input('interval-component', 'n_intervals')])
def update_table(n):
    # Load the new values from the existing dataframe
    predict_temp = predicted_data.sample(n=5)
    
    # Convert the dataframe to an HTML table
    table = html.Table([
        html.Thead(html.Tr([html.Th(col, style={'border-right': '1px solid black', 'border-bottom': '1px solid black'})
                             for col in predict_temp.columns])),
        html.Tbody([
            html.Tr([
                html.Td(predict_temp.iloc[i][col], style={'border-right': '1px solid black'})
                  for col in predict_temp.columns
            ]) for i in range(len(predict_temp))
        ])
    ])
    
    # Return the HTML table
    return table

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True, host = '127.0.0.1', port = 4200 )