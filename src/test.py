import pandas as pd
import pickle

df = pd.read_pickle('src/scrape_games/error_list.pkl')
print(df)