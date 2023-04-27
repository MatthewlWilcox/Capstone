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
data = pd.read_pickle('data/final_datasets/data_standardized.pkl')

# data = data[data['division'].isin(['E0', 'D1','I1', 'SP1', 'F1'])]
data = data.dropna(subset = ['B365A', 'BWH', 'WHH', 'VCD','BbMx>2.5',
                             'BbAv>2.5', 'BbMx<2.5', 'BbAv<2.5', 'std_attend', 'standard_attend'])
data = data.drop(['url', 'date_time'], axis =1)
obj_data = data.select_dtypes(include=['object']).copy()
column_obj_name = obj_data.columns.values.tolist()
print(column_obj_name)
print(data.dtypes)

label_encoder = LabelEncoder()


for obj in column_obj_name:
    data[obj] = label_encoder.fit_transform(data[obj])
data = data.astype(float)
data = data.dropna()
print(data.dtypes)

print(data.isna().sum())
print(data)


x = data.drop(['raw_attendance', 'standard_attend', 'capacity_filled'], axis = 1)
x = x[['home_team', 'away_team', 'division', 'date', 'time', 'day_of_week','B365H', 'B365D',
       'B365A']]
y = data['raw_attendance']

x_train, x_test, y_train, y_test = train_test_split(x,y, test_size = .2, random_state = 11)

def evaluate(model, test_features, test_labels):
    predictions = model.predict(test_features)
    errors = abs(predictions - test_labels)
    mape = 100 * np.mean(errors / test_labels)
    accuracy = 100 - mape
    print('Model Performance')
    print('Average Error: {:0.4f} degrees.'.format(np.mean(errors)))
    print('Accuracy = {:0.2f}%.'.format(accuracy))
    
    return accuracy
load_model = pickle.load(open('src/Modeling/Random_forest_model.sav', 'rb'))
evaluate(load_model, x_test, y_test)