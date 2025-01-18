# string = input()
# string = string[::-1]
# print(string)

# dic = {841: {"PetroBlitz" : "הכפר הירוק"}}
# for key in dic:
#     result = dic[key]
def team_name(dict: dict, team_number: int):
    return list(dic[team_number].keys())[0]

def team_location(dict: dict, team_number: int):
    """
    make sure the dictionarry is not a double dictionary.
    """
    team = team_name(dict, team_number)
    return dict[team_number][team]

dic = {841: {"PetroBlitz": "הכפר הירוק"}}

print (team_name(dic, 841))
print(team_location(dic, 841))