import pandas as pd
import pickle

df = pd.read_pickle('src/scrape_games/error_list.pkl')
print(df)
file = open('src\error_links.txt','w')
for i in df:
    file.write(i +'\n')
file.close()