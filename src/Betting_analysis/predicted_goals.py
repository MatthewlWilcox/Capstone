import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


data = pd.read_pickle('data/final_datasets/data_standardized.pkl')
data = data.dropna(subset = ['standard_attend', 'BbAv>2.5','BbAv<2.5'])
print(data)

increase_attend = []
higher_goals = []
for index, rows in data.iterrows():
    if rows['standard_attend'] >=0:
        increase_attend = increase_attend + [True]
    else:
        increase_attend = increase_attend + [False]
    if rows['BbAv>2.5'] <= rows['BbAv<2.5']:
        higher_goals = higher_goals + [True]
    else:
        higher_goals = higher_goals +[False]
print(increase_attend)

data['increase_attend'] = increase_attend
data['higher_goals'] = higher_goals
print(data)

df = data[['higher_goals', 'increase_attend']]
df = df.value_counts().reset_index(name= 'count')
count_pct = []
df_grouped_higher_goal_sum = df.groupby('higher_goals')['count'].sum().reset_index()
print(df_grouped_higher_goal_sum)


for index, rows in df.iterrows():
    print('----------')
    goals = rows['higher_goals']
    print(goals)
    total_count_goals = df_grouped_higher_goal_sum[df_grouped_higher_goal_sum['higher_goals'] == goals]['count'].values
    total_count_goals = sum(total_count_goals)
    print(total_count_goals)
    percent_total = rows['count']*100/total_count_goals
    print(percent_total)
    count_pct = count_pct + [percent_total]
df['count_pct'] = count_pct
# total_count = df['count'].sum()
# df['pct'] = df['count']*100/total_count
df = df.rename(columns = {'higher_goals':'Odds of Goals over 2.5 is greater', 'increase_attend': 'Increased Attendance'})
df2 = df.pivot(index = 'Odds of Goals over 2.5 is greater', columns = 'Increased Attendance', values = 'count_pct')
print(df)
sns.heatmap(data = df2, annot= True)
plt.gca().invert_xaxis()
# plt.gca().invert_yaxis()
plt.title('Predicted Goals in relation to Attendance')
plt.show()
sns.barplot(data =df, x = 'Odds of Goals over 2.5 is greater', y = 'count_pct', hue = 'Increased Attendance')
plt.gca().invert_xaxis()
plt.ylabel('Percent')
plt.title('Predicted Goals in relation to Attendance')
plt.show()
# print(df)
# df_to_plot = df[['Odds of Goals over 2.5 is greater', 'Increased Attendance', 'count_pct']]
# df_to_plot.set_index('Odds of Goals over 2.5 is greater').plot(kind = 'bar', stacked = True)
# plt.show()