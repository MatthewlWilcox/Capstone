import pandas as pd
import pickle
import numpy as np
data = pd.read_pickle('data/Data_to_change/complete_data.pkl')


data2 = data[pd.isnull(data['B365H'])]
print(data2)