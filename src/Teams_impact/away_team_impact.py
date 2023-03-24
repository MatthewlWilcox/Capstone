import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_pickle('data/final_datasets/data_standardized.pkl')
print(data)

away_team_impact = data.groupby(['away_team', 'division'])['standard_attend'].mean().reset_index()



div_dict = {'D1':'Bundesliga', 'D2': '2. Bundesliga', 'E0':'Premier League', 'E1':'Championship', 
            'E2':'League 1', 'E3':'Leauge 2','SP1':'La Liga Primera', 'SP2':'La Liga Segunda',
              'B1':'Jupiler League', 'F1':'Ligue 1','F2':'Ligue 2','I1':'Serie A','I2':'Seire B', 
              'SC0':'Scotish Premier League', 'SC1':'Scotish Division 1', 'T1':'Fubol Ligi 1', 'P1': 'Liga 1'}
divisions_list =['D1', 'D2', 'E0', 'E1', 'E2', 'E3', 'SP1' ,'SP2', 'B1', 'F1', 'F2', 'I1', 'I2', 'SC0', 'SC1', 'T1', 'P1']
away_team_impact_top30 = pd.DataFrame(columns = ['away_team', 'division', 'standard_attend'])
print(away_team_impact_top30)
for i in divisions_list:
    temp_impact_df = away_team_impact[away_team_impact['division'] == i].sort_values('standard_attend',ascending = False).head(3)
    away_team_impact_top30 = away_team_impact_top30.append(temp_impact_df)
# print(top_team_list)
# away_team_impact_top30 = away_team_impact[away_team_impact['away_team'].isin(top_team_list)]

# away_team_impact_top30 = away_team_impact[away_team_impact['division'] == 'E0']

away_team_impact_top30 = away_team_impact_top30.sort_values('division', ascending = False)
print(away_team_impact_top30)
away_team_impact_top30 = away_team_impact_top30.replace({'division':div_dict})

sns.barplot(data = away_team_impact_top30, x = 'standard_attend', y = 'away_team', hue = 'division', dodge = False)
plt.show()