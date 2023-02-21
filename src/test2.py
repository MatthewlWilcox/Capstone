import pandas as pd

x = pd.read_pickle('src\Data_Processing\Key_dictionary.pkl')
df = pd.DataFrame.from_dict(x,orient = 'index')
print(df)
df.to_csv('src/Data_Processing/key_dictionary_view.csv')