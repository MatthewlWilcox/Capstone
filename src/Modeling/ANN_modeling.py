import math
import pandas as pd
import tensorflow as tf
import matplotlib.pyplot as plt
from tensorflow.keras import Model
from tensorflow.keras import Sequential
from tensorflow.keras.optimizers import Adam
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.layers import Dense, Dropout
from sklearn.model_selection import train_test_split
from tensorflow.keras.losses import MeanSquaredLogarithmicError


data = pd.read_pickle('data/final_datasets/data_standardized.pkl')

data = data[data['division'].isin(['E0', 'D1','I1', 'SP1', 'F1'])]
data = data.dropna(subset = ['B365A', 'BWH', 'WHH', 'VCD','BbMx>2.5',
                             'BbAv>2.5', 'BbMx<2.5', 'BbAv<2.5', 'std_attend', 'standard_attend'])
data = data.drop(['url', 'date_time'], axis =1)
obj_data = data.select_dtypes(include=['object']).copy()
column_obj_name = obj_data.columns.values.tolist()
print(column_obj_name)
print(data.dtypes)

for obj in column_obj_name:

    data[obj] = data[obj].astype('category').cat.codes
data = data.astype(float)
data = data.dropna()

x = data.drop(['raw_attendance', 'standard_attend', 'capacity_filled'], axis = 1)
x = x[['home_team', 'away_team', 'division', 'date', 'time', 'day_of_week','B365H', 'B365D',
       'B365A']]
y = data['raw_attendance']

x_train, x_test, y_train, y_test = train_test_split(x,y, test_size = .2, random_state = 11)
def scale_datasets(x_train, x_test):
  standard_scaler = StandardScaler()
  x_train_scaled = pd.DataFrame(
      standard_scaler.fit_transform(x_train),
      columns=x_train.columns
  )
  x_test_scaled = pd.DataFrame(
      standard_scaler.transform(x_test),
      columns = x_test.columns
  )
  return x_train_scaled, x_test_scaled
x_train_scaled, x_test_scaled =  scale_datasets(x_train, x_test)

hidden_units1 = 300
hidden_units2 = 1000
hidden_units3 = 386
learning_rate = 0.01
def build_model_using_sequential():
  model = Sequential([
    Dense(hidden_units1, kernel_initializer='normal', activation='relu'),
    Dropout(0.2),
    Dense(hidden_units2, kernel_initializer='normal', activation='relu'),
    Dropout(0.2),
    Dense(hidden_units3, kernel_initializer='normal', activation='relu'),
    Dense(1, kernel_initializer='normal', activation='linear')
  ])
  return model
model = build_model_using_sequential()

msle = MeanSquaredLogarithmicError()
model.compile(
    loss=msle, 
    optimizer=Adam(learning_rate=learning_rate), 
    metrics=[msle]
)
# train the model
history = model.fit(
    x_train_scaled.values, 
    y_train.values, 
    epochs=20, 
    batch_size=64,
    validation_split=0.2
)

def plot_history(history, key):
  plt.plot(history.history[key])
  plt.plot(history.history['val_'+key])
  plt.xlabel("Epochs")
  plt.ylabel(key)
  plt.legend([key, 'val_'+key])
  plt.show()
# Plot the history
plot_history(history, 'mean_squared_logarithmic_error')
import numpy as np
from sklearn import metrics
x_test['predict'] = model.predict(x_test_scaled)
x_test['real'] = y_test
print(x_test)
errors = abs(x_test['predict'] - y_test) 
mape = 100*(errors/y_test)
accuracy = 100-np.mean(mape)
print('Average absolute error:', round(np.mean(errors), 2), 'degrees.')
print('Accuracy:', round(accuracy, 2), '%.')

rscore = metrics.r2_score(y_test, x_test['predict'])

print(rscore)
