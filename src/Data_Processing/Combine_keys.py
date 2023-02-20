import pandas as pd
import pickle

x = pd.read_pickle('src/Data_Processing/key.pkl')
y= pd.read_pickle('src/Data_Processing/key2.pkl')

combo_key = x + y
final_combo_key = []
print(combo_key)

for i in combo_key:
    first_val = i[0]
    second_val = i[1]
    if len(first_val)>= len(second_val):
        key_val = (second_val,first_val)
    else:
        key_val = (first_val,second_val)
    final_combo_key = final_combo_key +[key_val]

dict_final_key = dict(final_combo_key)

with open('src/Data_Processing/Key_dictionary.pkl','wb') as pick:
    pickle.dump(dict_final_key, pick)
