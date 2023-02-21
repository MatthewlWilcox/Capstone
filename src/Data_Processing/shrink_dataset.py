import pandas as pd


data = pd.read_pickle('data/Data_to_change/complete_data.pkl')


data = data[['home_team','home_score','away_team','away_score','day_of_week','month','day_of_month','year','time','attendance','stadium_x','a_href','Hohome_teammeTeam','date','Div','Date','HomeTeam','AwayTeam','FTHG','FTAG','FTR','HTHG','HTAG','HTR','B365H','B365D','B365A','BWH','BWD','BWA','WHH','WHD','WHA','VCH','VCD','VCA','BbMx>2.5','BbAv>2.5','BbMx<2.5','BbAv<2.5','index','stadium_y','City','Country','Capacity','url','_merge']]

# print(data)
x = 0

data2 = data[data['year']<= 2019]

div= []
for index, row in data2.iterrows():
    if  row['home_team'] != row['HomeTeam']:
        division = row['Div']
        div = div + [division]
        x += 1





print(div)


counts={}
for i in div:
    if i in counts:
        counts[i] = counts[i] + 1
    else:
        counts[i] = 1


print(counts)




# print(x/len(data['home_team']))