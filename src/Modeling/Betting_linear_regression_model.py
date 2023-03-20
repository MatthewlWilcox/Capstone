import pandas as pd
import statsmodels.api as sm

bet_data = pd.read_pickle('data/final_datasets/data_standardized.pkl')
bet_data = bet_data.dropna()
print(bet_data.columns)
x = bet_data[['B365H', 'B365D', 'B365A', 'BbAv>2.5', 'BbAv<2.5']]
y = bet_data['raw_attendance']

x = sm.add_constant(x)
model = sm.OLS(y,x).fit()
y_standardized = bet_data['standard_attend']
model_standard = sm.OLS(y_standardized, x).fit()
print(model.summary())
print(model_standard.summary())
# print(bet_data.columns)