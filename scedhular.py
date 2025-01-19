##Scedhule
import json
import random

judging_rooms = 4
Robot_tables = 4

with open("data.txt", "r") as file:
    teams = json.load(file)

def cycle(list):
    return [list[-1]] + list[:-1]

print(cycle(["A", "B", "C", "D"]))
team_amount = len(teams)

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




for i in range(robot_rounds + judging_rounds):

    N = (team_amount * 0.75).__floor__() - 1
    first75 = team_keys[0:N]
    print(first75)
