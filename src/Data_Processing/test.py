# import pickle
# with open('src/Data_Processing/not_in_both.pkl', 'rb') as pick:
#     print(pickle.load(pick))
# with open('src/Data_Processing/key.pkl', 'rb') as pick:
#     print(len(pickle.load(pick)))
# with open('src/Data_Processing/list_2_not_found.pkl', 'rb') as pick:
#     print(pickle.load(pick))
team = 'manchester_united'

l = len(team)
print(team[0:l])
# team_str_len = len(team)

# n = team_str_len
# divis = range(1,n,1)
# print(list(divis))
# x = 1
# for divider in divis:
#     temp_n = n//divider
#     print(temp_n)
#     broken_str = [(team[i:i+temp_n]) for i in range(0,len(team), temp_n)]
#     print(x)
#     print(broken_str[0:x])
#     x = x + 1
#     print(x)
#     if temp_n == 1:
#         break


