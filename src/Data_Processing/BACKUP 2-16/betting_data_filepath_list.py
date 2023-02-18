import pandas as pd
import os
import pickle


directory = 'data/RAWDATA/Football-dataBettingData'
file_list = []
for f in os.listdir(directory):
    folder = os.path.join(directory, f)
    for fi in os.listdir(folder):
        print(fi)
        file = os.path.join(folder, fi)
        print(file)
        if os.path.isfile(file):
            file_list.append(file)
            print(file)
print(file_list)
with open("src/Data_Processing/betting_file_list.bin", "wb") as pick:
    pickle.dump(file_list, pick)


