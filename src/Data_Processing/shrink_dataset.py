import pandas as pd


data = pd.read_pickle('data/Data_to_change/complete_data_before_2019.pkl')


data = data[['home_team','away_team','home_score','away_score','date','time','day_of_week','attendance','stadium_y','City','Country','Capacity','url','Div','FTHG','FTAG','FTR','HTHG','HTAG','HTR','B365H','B365D','B365A','BWH','BWD','BWA','WHH','WHD','WHA','VCH','VCD','VCA','BbMx>2.5','BbAv>2.5','BbMx<2.5','BbAv<2.5']]

print(data)


data.to_pickle("data/Data_to_change/complete_data_2010_2019_shrunk.pkl")
data.to_csv("data/Data_to_change/complete_data_2010_2019_shrunk.csv")


# x = 0

# data2 = data[data['year']<= 2019]
# print(data)
# div= []
# for index, row in data2.iterrows():
#     if  row['home_team'] != row['HomeTeam']:
#         division = row['Div']
#         div = div + [division]
#         x += 1





# print(len(div))


# counts={}
# for i in div:
#     if i in counts:
#         counts[i] = counts[i] + 1
#     else:
#         counts[i] = 1


# # print(counts)




# print(x/len(data['home_team']))