import pandas as pd
import numpy as np
import sys
data = pd.read_pickle('data/Data_to_change/complete_data.pkl')

print(data)

# with open('src/Data_processing/na_sum.txt', 'w') as f:
#     sys.stdout = f
#     for column in data.columns:
#         print(column, data[column].isnull().sum())
#     sys.stdout = sys.__stdout__

data = data[data['year']<=2019]
print(data)
leagues = data['Div'].unique()
print(leagues)
na_columns =['div', 'size'] +list(data.columns)
print(na_columns)
na_dataframe = pd.DataFrame(columns = na_columns)
print(na_dataframe)

for league in leagues:
  df = data[data['Div']==league]
  na_list = [league, len(df)]
  for column in df.columns:
    na_list = na_list + ["%.2f" % (df[column].isnull().sum()/len(df[column])*100)]
  print(na_list)
  na_dataframe.loc[len(na_dataframe)] = na_list
  
na_dataframe.to_csv('src/Data_processing/na_leagues.csv')
print(na_dataframe)

# for league in leagues:
#     df = data[data['Div'] == league]
#     address = 'src/Data_processing/na_by_league/'+str(league)+'summary.txt'
#     with open(address, 'w') as f:
#         sys.stdout = f
#         print("League: ", league)
#         print('#'*30)
#         print("Years \n Max Year:", df['year'].max(), '\n Min Year', df['year'].min())
#         print('#'*30)
#         try:
#           print(df.head())
#         except:
#           print('Error')
#         print('#'*30)

#         for column in df.columns:
#           print(column, df[column].isnull().sum())
#         sys.stdout = sys.__stdout__
#     print('DONE ', league)


