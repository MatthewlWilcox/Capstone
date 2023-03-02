import pandas as pd
import plotly.express as px


df = pd.read_pickle('data/final_datasets/total_data.pkl')
print(df.columns)
df = df[[
    'date', 'time', 'day_of_week', 'date_time', 'raw_attendance', 'capacity_filled', 'division'
]]
df['month_year']= df['date'].dt.
print(df)
df_grouped = df.groupby(['date', 'division']).median().reset_index()
print(df_grouped)

fig = px.line(df_grouped, x = 'date', y ='raw_attendance', color = 'division')
fig.show()