import pandas as pd
import numpy as np

data = pd.read_pickle('data/final_datasets/Total_data.pkl')

bet_dataset = data[['home_score', 'away_score',
        'raw_attendance','capacity', 'division', 'FTHG', 'FTAG', 'FTR', 'HTHG', 'HTAG',
       'HTR', 'B365H', 'B365D', 'B365A', 'BWH', 'BWD', 'BWA', 'WHH', 'WHD',
       'WHA', 'VCH', 'VCD', 'VCA', 'BbMx>2.5', 'BbAv>2.5', 'BbMx<2.5',
       'BbAv<2.5', 'capacity_filled']]

b365_conditions = [(bet_dataset['B365H'] < bet_dataset['B365A']) & (bet_dataset['B365H'] < bet_dataset['B365D']),
                   (bet_dataset['B365A'] < bet_dataset['B365H']) & (bet_dataset['B365A'] < bet_dataset['B365D']),
                   (bet_dataset['B365D'] < bet_dataset['B365A']) & (bet_dataset['B365D'] < bet_dataset['B365H'])]

b365_vals = ['H', 'A', 'D']
bet_dataset['B365_Result'] = np.select(b365_conditions,b365_vals)

bw_conditions = [(bet_dataset['BWH'] < bet_dataset['BWA']) & (bet_dataset['BWH'] < bet_dataset['BWD']),
                   (bet_dataset['BWA'] < bet_dataset['BWH']) & (bet_dataset['BWA'] < bet_dataset['BWD']),
                   (bet_dataset['BWD'] < bet_dataset['BWA']) & (bet_dataset['BWD'] < bet_dataset['BWH'])]

bw_vals = ['H', 'A', 'D']
bet_dataset['BW_Result'] = np.select(bw_conditions,bw_vals)

wh_conditions = [(bet_dataset['WHH'] < bet_dataset['WHA']) & (bet_dataset['WHH'] < bet_dataset['WHD']),
                   (bet_dataset['WHA'] < bet_dataset['WHH']) & (bet_dataset['WHA'] < bet_dataset['WHD']),
                   (bet_dataset['WHD'] < bet_dataset['WHA']) & (bet_dataset['WHD'] < bet_dataset['WHH'])]

wh_vals = ['H', 'A', 'D']
bet_dataset['WH_Result'] = np.select(wh_conditions,wh_vals)

vc_conditions = [(bet_dataset['VCH'] < bet_dataset['VCA']) & (bet_dataset['VCH'] < bet_dataset['VCD']),
                   (bet_dataset['VCA'] < bet_dataset['VCH']) & (bet_dataset['VCA'] < bet_dataset['VCD']),
                   (bet_dataset['VCD'] < bet_dataset['VCA']) & (bet_dataset['VCD'] < bet_dataset['VCH'])]

vc_vals = ['H', 'A', 'D']
bet_dataset['VC_Result'] = np.select(vc_conditions,vc_vals)

print(bet_dataset[['B365H', 'B365D', 'B365A', 'B365_Result', 'BWH', 'BWA', 'BWD', 'BW_Result',
                   'BWH', 'BWA', 'BWD', 'BW_Result', 'WHH', 'WHA', 'WHD', 'WH_Result', 'VCH', 
                   'VCA', 'VCD', 'VC_Result'
                   ]])

bet_dataset.to_pickle('data/final_datasets/bet_data.pkl')
bet_dataset.to_csv('data/final_datasets/bet_data.csv')
