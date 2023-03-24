import pandas as pd


data = pd.read_pickle('data/final_datasets/data_standardized.pkl')
data = data.dropna(subset = ['standard_attend', 'BbAv>2.5','BbAv<2.5'])
print(data)

increase_attend = []
higher_goals = []
for index, rows in data.iterrows():
    if rows['standard_attend'] >=0:
        increase_attend = increase_attend + [True]
    else:
        increase_attend = increase_attend + [False]
    if rows['BbAv>2.5'] >= rows['BbAv<2.5']:
        higher_goals = higher_goals + [True]
    else:
        higher_goals = higher_goals +[False]
print(increase_attend)

data['increase_attend'] = increase_attend
data['higher_goals'] = higher_goals
print(data)

df = data[['higher_goals', 'increase_attend']]
print(df.value_counts())