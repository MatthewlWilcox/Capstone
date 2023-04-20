import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go


data = pd.read_pickle('data/final_datasets/data_standardized.pkl')

away_team_impact = data.groupby(['away_team', 'division'])['standard_attend'].mean().reset_index()


# away_team_impact = away_team_impact[away_team_impact['division'].isin(['E3', 'E1', 'E2'])]
div_dict = {'D1':'Bundesliga', 'D2': '2. Bundesliga', 'E0':'Premier League', 'E1':'Championship', 
            'E2':'League 1', 'E3':'Leauge 2','SP1':'La Liga Primera', 'SP2':'La Liga Segunda',
              'B1':'Jupiler League', 'F1':'Ligue 1','F2':'Ligue 2','I1':'Serie A','I2':'Seire B', 
              'SC0':'Scotish Premier League', 'SC1':'Scotish Division 1', 'T1':'Fubol Ligi 1', 'P1': 'Liga 1'}
divisions_list =['D1', 'D2', 'E0', 'E1', 'E2', 'E3', 'SP1' ,'SP2', 'B1', 'F1', 'F2', 'I1', 'I2', 'SC0', 'SC1', 'T1', 'P1']

away_team_impact = away_team_impact[['away_team', 'division', 'standard_attend']]
print(away_team_impact)


from dash import Dash, dcc, html, Input, Output

import plotly.graph_objects as go
import plotly.express as px
# fig = go.Figure(px.bar(away_team_impact, y= 'away_team', x = 'standard_attend', color = 'division'))

app = Dash(__name__)
app.layout = html.Div(id = 'parent', children = [
    html.H1(id = 'H1', children = 'Away Team Impact'),
    dcc.Slider(0,20,1, value =3,id = 'number_of_teams'),
    dcc.Dropdown(id = 'dropdown', 
                 options = [
                {'label': 'Bundesliga', 'value':'D1'},
                {'label': '2. Bundesliga', 'value':'D12'},
                {'label': 'Premier League', 'value':'E0'},
                {'label': 'Championship', 'value':'E1'},
                {'label': 'League 1', 'value':'E2'},
                {'label': 'Leauge 2', 'value':'E3'},
                {'label': 'La Liga Primera', 'value':'SP1'},
                {'label': 'La Liga Segunda', 'value':'SP2'},
                {'label': 'Jupiler League', 'value':'B1'},
                {'label': 'Ligue 1', 'value':'F1'},
                {'label': 'Ligue 2', 'value':'F2'},
                {'label': 'Serie A', 'value':'I1'},
                {'label': 'Serie B', 'value':'I2'},
                {'label': 'Scotish Premier League', 'value':'SC0'},
                {'label': 'Scotish Division 1', 'value':'SC1'},
                {'label': 'Fubol Ligi 1', 'value':'T1'},
                {'label': 'Liga 1', 'value':'P1'}


                 ], value = 'E0',
                 multi = True),
    dcc.Graph(id = 'bar_plot', figure=px.bar(away_team_impact, y='away_team', x='standard_attend', color='division'))
])

@app.callback(
    Output("bar_plot", "figure"), 
    [Input("dropdown", "value")]
    )
def update_graph(value):
    # print(value)
    df = away_team_impact
    df = df[df['division'].isin(value)]
    fig = px.bar(df,y= 'away_team', x= 'standard_attend', color = 'division')
    return fig
if __name__ == '__main__':
    app.run_server()

# for i in divisions_list:
#     temp_impact_df = away_team_impact[away_team_impact['division'] == i].sort_values('standard_attend',ascending = False).head(3)
#     away_team_impact_top30 = away_team_impact_top30.append(temp_impact_df)






# print(top_team_list)
# away_team_impact_top30 = away_team_impact[away_team_impact['away_team'].isin(top_team_list)]

# away_team_impact_top30 = away_team_impact[away_team_impact['division'] == 'E0']


# away_team_impact_top30 = away_team_impact_top30.sort_values('division', ascending = False)
# print(away_team_impact_top30)
# away_team_impact_top30 = away_team_impact_top30.replace({'division':div_dict})
# away_team_impact_top30['away_team']  = away_team_impact_top30['away_team'].str.replace('_', ' ')
# away_team_impact_top30['away_team']  = away_team_impact_top30['away_team'].str.upper()
# print(away_team_impact_top30)
# sns.barplot(data = away_team_impact_top30, x = 'standard_attend', y = 'away_team', hue = 'division', dodge = False)
# plt.title('Away Teams Impact on Attendance: Top 3 Teams per English League')
# plt.xlabel('Average Increase on Home Teams Attendnace')
# plt.ylabel('Away Team')
# # plt.legend(bbox_to_anchor=(1, 1), loc='upper left', borderaxespad=0)
# # plt.savefig('results/Away_team_impact_top.png')
# plt.show()