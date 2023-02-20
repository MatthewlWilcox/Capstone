import pandas as pd
import pickle

x = pd.read_pickle('data/Data_to_change/betting_data_updated_names.pkl')
y= pd.read_pickle('src/Data_Processing/Key_dictionary.pkl')
print(x)
# print(y)