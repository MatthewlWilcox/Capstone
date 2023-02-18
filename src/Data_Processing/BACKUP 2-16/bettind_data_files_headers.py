import pickle
import pandas as pd
df = pd.DataFrame()
file_list = []
file_header = []
with open('src/Data_Processing/betting_file_list.bin', 'rb') as pick:
    file_list =pickle.load(pick)
for file in file_list:
    temp_df = pd.read_csv(file,encoding= 'latin1')
    df = pd.concat([df, temp_df])

df.to_csv("data/betting_data.csv")
