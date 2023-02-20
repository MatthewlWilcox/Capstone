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




with open('src/Data_Processing/not_in_both.pkl', 'rb') as pick:
    betting_error_teams = pickle.load(pick)
with open('src/Data_Processing/match_error_teams.pkl', 'rb') as pick:
    match_error_teams = pickle.load(pick)


temp_list1 = ['man_city', 'man_u', 'norwhich', 'test3']
temp_list2 = ['manchester_city', 'manchester_united', 'norwich_city', 'milan' , 'test3']



def find_pair_in_list(list1, list2):
    # betting_error_teams = list1
    # match_error_teams = list2

    list1 = list1
    list2 = list2
    not_in_both = []
    key = []
    for team in list1:
        print("#"*50)
        print("List 1 Team:", team)
        print("-"*50)
        # n = 3
        # broken_str = [(team[i:i+n]) for i in range(0,len(team), n)] 
        # temp_num = 0
        temp_list_2 =[]
        broken_str =[]
        team_str_len = len(team)
        # n = team_str_len
        # while n != 0:
        #     broken_str = [(team[i:i+n]) for i in range(0,len(team), n)]
        #     n = n - 1 

        # n = team_str_len
        # divis = range(1,n,1)
        # print(list(divis))
        # x = 1
        # for divider in divis:
        #     temp_n = n//divider
        #     temp_broken_str = [(team[i:i+temp_n]) for i in range(0,len(team), temp_n)]
        #     broken_str=  broken_str +(temp_broken_str[0:x])
        #     x = x + 1
        #     if temp_n == 1:
        #         break
        stop_num = len(team) +1
        while team_str_len != 0: 
            first_character = 0
            last_character = team_str_len
            while last_character != stop_num:
                temp_str = team[first_character:last_character]
                
                last_character = last_character +1
                first_character = first_character +1
                broken_str = broken_str + [temp_str]
            team_str_len = team_str_len - 1

     

        temp_potential_matching_teams = []
        temp_team2_list = set(list2)

        for string in broken_str:
            for temp_team in temp_team2_list:
                if temp_team.__contains__(string):
                    temp_potential_matching_teams = temp_potential_matching_teams + [temp_team]
                 
                
        
        temp_pot_match_team_nodup   = [ ]
        [temp_pot_match_team_nodup.append(x) for x in temp_potential_matching_teams if x not in temp_pot_match_team_nodup]
        temp_pot_match_team_nodup.reverse()
        sleep(1.0)
        os.system('cls')
        if len(temp_potential_matching_teams) == 0:
            not_in_both.append(team)
            print("No Results Found")
        else:

            temp_num = 0
            for temp_team in temp_pot_match_team_nodup:
                print("|", temp_num, "| ", temp_team)
                temp_num += 1
            print("|", temp_num, "|  None of the above")
            print("#"*50)
            print("List 1 Team:", team)
            print("-"*50)
            while(True):
                in_num = input("Enter the correct teams number: ") or str(temp_num)


                while not in_num.isdigit():
                    in_num = input("Input must be numeric, please reenter: ")
                in_num = int(in_num)
                if in_num not in range(0,temp_num+1):
                    print("enter a valid number 0 - ", temp_num)

                else:
                    if in_num == temp_num:
                        q_temp_team = "None of the above"
                    else:
                        q_temp_team = temp_pot_match_team_nodup[in_num]
                    question_str = "Is " +q_temp_team + " = " + team + " correct?"
                    x = yes_or_no(question_str)
                    if x == True:
                        if in_num == temp_num:
                            not_in_both.append(team)
                        else:
                            key_value = (team, temp_pot_match_team_nodup[in_num])
                            print(key_value)
                            print(temp_pot_match_team_nodup[in_num])
                            print(temp_list2)
                            list2.remove(temp_pot_match_team_nodup[in_num])
                            key.append(key_value)
                        break

    return [key, not_in_both, list2]

x = find_pair_in_list(betting_error_teams, match_error_teams)
# print(x[0])
# print(x[1])
# print(x[2])
with open('src/Data_Processing/key2.pkl', 'wb') as pick:
    pickle.dump(x[0],  pick)
with open('src/Data_Processing/not_in_both2.pkl', 'wb') as pick:
    pickle.dump(x[1], pick)
with open('1src/Data_Processing/list_2_not_found2.pkl', 'wb') as pick:
    pickle.dump(x[2], pick)


