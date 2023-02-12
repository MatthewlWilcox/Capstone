import pickle
with open('src/Data_Processing/not_in_both.pkl', 'rb') as pick:
    print(len(pickle.load(pick)))
with open('src/Data_Processing/key.pkl', 'rb') as pick:
    print(len(pickle.load(pick)))
with open('src/Data_Processing/list_2_not_found.pkl', 'rb') as pick:
    print(pickle.load(pick))