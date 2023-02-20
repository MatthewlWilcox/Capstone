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



leagues = data['Div'].unique()
print(leagues)

for league in leagues:
    df = data[data['Div'] == league]
    address = 'src/Data_processing/na_by_league/'+str(league)+'summary.txt'
    with open(address, 'w') as f:
        sys.stdout = f
        print("League: ", league)
        print('#'*30)
        print("Years \n Max Year:", df['year'].max(), '\n Min Year', df['year'].min())
        print('#'*30)
        print(df.head().to_string().encode('latin-1'))
        print('#'*30)

        for column in df.columns:
          print(column, df[column].isnull().sum())
        sys.stdout = sys.__stdout__
    print('DONE ', league)