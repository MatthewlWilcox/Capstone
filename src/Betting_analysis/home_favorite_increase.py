import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

bet_data = pd.read_pickle('data/final_datasets/data_standardized.pkl')
bet_data = bet_data.dropna(subset = ['B365H', 'B365A'])
h_fav = []
attend_increase = []
for index, rows in bet_data.iterrows():
    if rows['B365H'] < rows['B365A']:
        h_fav = h_fav + [True]
    else:
        h_fav = h_fav + [False]
    if rows['standard_attend'] >= 0:
        attend_increase = attend_increase + [True]
    else:
        attend_increase = attend_increase + [False]
print(h_fav)
        
bet_increase_bool = bet_data
bet_increase_bool['home_fav'] = h_fav
bet_increase_bool['attend_increase'] = attend_increase
bet_bool = bet_increase_bool[['home_fav', 'attend_increase','raw_attendance']]
bet_bool = bet_bool.groupby(['home_fav', 'attend_increase']).count().reset_index().rename(columns = {'home_fav':'Home Team Favorited', 'attend_increase':'Increase In Attendance'})
# total_matches = sum(bet_bool['raw_attendance'])
# bet_bool['raw_attendance'] = bet_bool['raw_attendance'] *100/total_matches

print(bet_bool)
# print(total_matches)
count_pct = []
for index, rows in bet_bool.iterrows():
    print('----------')
    goals = rows['Home Team Favorited']
    print(goals)
    total_count_goals = bet_bool[bet_bool['Home Team Favorited'] == goals]['raw_attendance'].values
    total_count_goals = sum(total_count_goals)
    print(total_count_goals)
    percent_total = rows['raw_attendance']*100/total_count_goals
    print(percent_total)
    count_pct = count_pct + [percent_total]
bet_bool['pcnt_values']  = count_pct


# bet_bool = bet_bool.pivot_table(values = 'pcnt_values', index = 'Home Team Favorited', columns = 'Increase In Attendance')
print(bet_bool)

# sns.heatmap(bet_bool,annot= True)
sns.barplot(data =bet_bool, x = 'Home Team Favorited', y = 'pcnt_values', hue = 'Increase In Attendance')

plt.gca().invert_xaxis()
# plt.gca().invert_yaxis()
plt.title('Attendance Impact depending if Home Team is Favored')
plt.ylabel('Percent')
plt.show()





