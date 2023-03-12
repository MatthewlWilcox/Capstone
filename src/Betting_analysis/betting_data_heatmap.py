import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


bet_data = pd.read_pickle('data/final_datasets/bet_data.pkl')
def betting_accuracy_vis(name):
    b365_data = bet_data[[name, 'FTR']].dropna()
    # print(b365_data[name].value_counts())
    b365_data = b365_data[b365_data[name]!= '0']
    b365_data = b365_data.groupby(['FTR',name]).size()
    b365_data = b365_data.reset_index(name = 'count')
    FTR_result = b365_data[[name,'count']].rename(columns = {'count':'total'})
    FTR_result = FTR_result.groupby([name]).sum().reset_index()
    # print(FTR_result)
    b365_data = pd.merge(b365_data, FTR_result, on =name)
    total_count = b365_data['count'].sum()
    # print(total_count)
    b365_data['pct'] = b365_data['count']/b365_data['total'] *100
    # print(b365_data)
    b365_data = b365_data.pivot(index = 'FTR', columns = name, values = 'pct')
    # print(b365_data)

    fig = sns.heatmap(data = b365_data, annot= True)
    plt.title(name + ' Accuracy in predicting Actual Result')
    
    plt.savefig('results/betting/' + name + '.png', dpi = 1200)
    plt.show()

result_name_list = ['B365_Result', 'BW_Result', 'WH_Result', 'VC_Result']
for i in result_name_list:
    betting_accuracy_vis(i)
