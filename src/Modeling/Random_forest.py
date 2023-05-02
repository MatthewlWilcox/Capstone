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
model_dataset = pd.read_pickle('data/final_datasets/data_standardized.pkl')
 
model_dataset = model_dataset.dropna(subset = ['B365A', 'BWH', 'WHH', 'VCD','BbMx>2.5',
                             'BbAv>2.5', 'BbMx<2.5', 'BbAv<2.5', 'std_attend', 'standard_attend'])
model_dataset = model_dataset.drop(['date_time'], axis =1)
obj_data = model_dataset.select_dtypes(include=['object']).copy()
column_obj_name = obj_data.columns.values.tolist()
before_encode = model_dataset[['division', 'home_team', 'away_team']]

label_encoder = LabelEncoder()
post_encode = model_dataset[['division', 'home_team', 'away_team']]

encode_compare = pd.concat([before_encode, post_encode], axis = 1, ignore_index=True)
encode_compare.columns = ['division', 'home_team', 'away_team', 'division_encode', 'home_encode', 'away_encode']
# print(encode_compare)

div_key = pd.Series(encode_compare.division.values, index = encode_compare.division_encode).to_dict()
home_key = pd.Series(encode_compare.home_team.values, index = encode_compare.home_encode).to_dict()
away_key = pd.Series(encode_compare.away_team.values, index = encode_compare.away_encode).to_dict()


for obj in column_obj_name:
    model_dataset[obj] = label_encoder.fit_transform(model_dataset[obj])
model_dataset = model_dataset.astype(float)
model_dataset = model_dataset.dropna()


x = model_dataset.drop(['raw_attendance', 'standard_attend'], axis = 1)
x = x[['home_team', 'away_team', 'division', 'date', 'time', 'day_of_week','B365H', 'B365D',
       'B365A']]
y = model_dataset['raw_attendance']

x_train, x_test, y_train, y_test = train_test_split(x,y, test_size = .2, random_state = 11)


# ------------------------------------------------------------------------------------------------------------------------------------------------
# Linear Regression
# ------------------------------------------------------------------------------------------------------------------------------------------------

lin_regressor = LinearRegression()
lin_regressor.fit(x_train, y_train)

linear_y_predict = lin_regressor.predict(x_test)
print(metrics.r2_score(y_test, linear_y_predict))
print(lin_regressor.score(x_test,y_test))

# ------------------------------------------------------------------------------------------------------------------------------------------------
# Polynomial Regression
# ------------------------------------------------------------------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------------------------------------------------------------------
# Random Forest
# ------------------------------------------------------------------------------------------------------------------------------------------------
random_forest_model = RandomForestRegressor(n_estimators = 1000, random_state= 11)

random_forest_model.fit(x_train, y_train)

pickle.dump(random_forest_model, open('Random_forest_model.sav', 'wb'))


y_predict = random_forest_model.predict(x_test)

mae = metrics.mean_absolute_error(y_test, y_predict)
mse = metrics.mean_squared_error(y_test, y_predict)
rmse = mse**.5
print(mae)
print(rmse)

# rmse = float(format(np.sqrt(mean_squared_error(y_test, y_pred)),'.3f'))

# print(rmse)


errors = abs(y_predict - y_test) 
# print(errors)


mape = 100*(errors/y_test)
accuracy = 100-np.mean(mape)
print('Average absolute error:', round(np.mean(errors), 2), 'degrees.')
print('Accuracy:', round(accuracy, 2), '%.')

rscore = metrics.r2_score(y_test, y_predict)

print(rscore)
plt.scatter(y_test, y_predict)
plt.xlim(0, 100000)
plt.ylim(0, 100000)
plt.ylabel('Predicted DT')
plt.xlabel('Actual DT')
plt.plot([0, 100000], [0, 100000], 'black')
plt.show()

# ------------------------------------------------------------------------------------------------------------------------------------------------