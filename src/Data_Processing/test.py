import pandas as pd
from sklearn.datasets import load_iris
data = load_iris()
df = pd.read_csv(r'data/RAWDATA/Football-dataBettingData\11-12\B1.csv')
print(df.to_string())