import pickle
import pandas as pd
import os
from time import sleep
# looks through one list and tries to find matches of another list. Will be mannual
def yes_or_no(question):
    reply = input(question+' (y/n): ').lower().strip() or 'y'
    if reply[0] == 'y':
        return True
    if reply[0] == 'n':
        return False
    else:
        return yes_or_no("Uhhhh... please enter ")




with open('src/Data_Processing/betting_error-team.pkl', 'rb') as pick:
    betting_error_teams = pickle.load(pick)
with open('src/Data_Processing/match_error_teams.pkl', 'rb') as pick:
    match_error_teams = pickle.load(pick)


temp_list1 = ['zzzzzzz','man_city', 'man_u', 'norwhich']
temp_list2 = ['manchester_city', 'manchester_united', 'norwich_city', 'milan' , 'test3']



def find_pair_in_list(list1, list2):
    betting_error_teams = list1
    match_error_teams = list2
    not_in_both = []
    key = []
    for team in betting_error_teams:
        print("#"*50)
        print("Betting Team list team:", team)
        print("-"*50)
        # n = 3
        # broken_str = [(team[i:i+n]) for i in range(0,len(team), n)] 
        # temp_num = 0
        # temp_match_team_list =[]
        broken_str =[]
        team_str_len = len(team)
        # n = team_str_len
        # while n != 0:
        #     broken_str = [(team[i:i+n]) for i in range(0,len(team), n)]
        #     n = n - 1 

        n = team_str_len
        divis = range(1,n,1)
        print(list(divis))
        x = 1
        for divider in divis:
            temp_n = n//divider
            print(temp_n)
            temp_broken_str = [(team[i:i+temp_n]) for i in range(0,len(team), temp_n)]
            broken_str.append(temp_broken_str[0:x])
            x = x + 1
            print(x)
            if temp_n == 1:
                break







        for match_team in match_error_teams:

            for str in broken_str:
                if str in match_team:
                    temp_match_team_list.append(match_team)
                    break
        if len(temp_match_team_list) == 0:
            not_in_both.append(team)
            print("No Results Found")
        else:
            temp_match_team_list = sorted(temp_match_team_list)
            for temp_team in temp_match_team_list:
                print("|", temp_num, "| ", temp_team)
                temp_num += 1
            print("|", temp_num, "|  None of the above")
            
            while(True):
                in_num = input("Enter the correct teams number: ")
                while not in_num.isdigit():
                    in_num = input("Input must be numeric, please reenter: ")
                in_num = int(in_num)
                if in_num not in range(0,temp_num+1):
                    print("enter a valid number 0 - ", temp_num)

                else:
                    if in_num == temp_num:
                        q_temp_team = "None of the above"
                    else:
                        q_temp_team = temp_match_team_list[in_num]
                    question_str = "Is " +q_temp_team + " = " + team + " correct?"
                    x = yes_or_no(question_str)
                    if x == True:
                        if in_num == temp_num:
                            not_in_both.append(team)
                        else:
                            key_value = (team, temp_match_team_list[in_num])
                            match_error_teams.remove(temp_match_team_list[in_num])
                            key.append(key_value)
                        break
        sleep(1.50)
        os.system('clear')
    return [key, not_in_both, match_error_teams]

x = find_pair_in_list(temp_list1, temp_list2)
# print(x[0])
# print(x[1])
# print(x[2])
# with open('src/Data_Processing/key.pkl', 'wb') as pick:
#     pickle.dump(x[0],  pick)
# with open('src/Data_Processing/not_in_both.pkl', 'wb') as pick:
#     pickle.dump(x[1], pick)
# with open('1src/Data_Processing/list_2_not_found.pkl', 'wb') as pick:
#     pickle.dump(x[2], pick)


