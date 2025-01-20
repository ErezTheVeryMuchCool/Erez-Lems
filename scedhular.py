##Scedhule
import json
import random
import math


judging_rooms = 4
Robot_tables = 4

with open("data.txt", "r") as file:
    teams = json.load(file)

def cycle(list):
    return [list[-1]] + list[:-1]     

print(cycle(["A", "B", "C", "D"]))
team_amount = len(teams)
if team_amount % 2 != 0:
    teams["0" : {"Err" : "or"}]
# declering rounds
training_event = True
robot_events_per_team = 4

robot_rounds = team_amount * robot_events_per_team / 2
judging_rounds = (team_amount / judging_rooms).__ceil__()

print(robot_rounds)

start_time_hour = 9
start_time_minute = 0


# team = random.randint(0, team_amount - 1)
# team = teams[team]


team_keys = list(teams.keys())
random.shuffle(team_keys)
print(team_keys)

def calculate40(list):
    N = (team_amount * 0.40).__floor__() - 1
    first75 = list[0:N]
    return first75

def calculate40(list):
    N = (team_amount * 0.40).__floor__() - 1
    first75 = list[0:N]
    return first75

['941', '123', '841', '1695', '1097', '3388', '380']
['380', '941', '123', '841', '1695', '1097', '3388']

all_rounds = {}

for i in range(int(robot_rounds + judging_rounds)):
    first40 = calculate40(team_keys)
    newList = team_keys
    # newList = cycle(team_keys)
    ### robot rounds:
    temp_list = []
    for i in range(0, team_amount, 2):
        team1 = newList[i]
        team2 = newList[i+1]
        all_rounds.update({i/2 : [team1,team2]})
        temp_list.append(team1)
        temp_list.append(team2)
    
    while True:
        last_list = newList
        random.shuffle(newList)
        first40 = calculate40(newList)
        if len(set(first40) & set(calculate40(last_list))) == 0:
            break

    for i in range(0, team_amount, 2):
        team1 = newList[i]
        team2 = newList[i+1]
        all_rounds.update({i/2 : [team1,team2]})

    print(all_rounds)