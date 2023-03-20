import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_pickle('data/final_datasets/data_standardized.pkl')
data = data[data['division']!= 'SC2']
data = data[['day_of_week', 'raw_attendance', 'standard_attend', 'division']]
data = data.groupby(['day_of_week', 'division']).count()
data = data['raw_attendance'].dropna().reset_index().pivot(index = 'day_of_week' , columns = 'division', values = 'raw_attendance')
print(data)
print('done')
data.plot(kind = 'bar', stacked = True )
plt.show()