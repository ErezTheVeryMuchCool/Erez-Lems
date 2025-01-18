import re
import json

def get_team_numbers(dict):
    """
    gets all team numbers from a dict.

    parameter: python dictionary

    returns: all the keys(t eam numbers) of a team.

    this function allows for the code to stay organized and sweeettt
    """
    return list(dict.keys())
def team_name(dict: dict, team_number: int):
    return list(dict[team_number].keys())[0]

def team_location(dict: dict, team_number: int):
    """
    please make sure the dictionarry is not a double dictionary.
    """
    team = team_name(dict, team_number)
    return dict[team_number][team]

def contains_hebrew(text): #checks if name contains at all any hebrew characters
    hebrew = re.compile(r'[\u0590-\u05FF]')
    return bool(hebrew.search(text))

def flip_hebrew(text):
    if contains_hebrew(text) == True:
            return text[::-1]
    else:
        return text

def add_teams(teams = {}, save = False, file = "data.json"):
    """
    generates a team list for a global database, competition, etc.

    *Parameter*: if you want to add to an already existing dict of teams, enter the dictionary there.

    The function returns a 3D dict.
    key; team number, eg. 1234 (Int)
    item; dict of team name and team place. eg. "StarBlitz":"הכפר הירוק"
    
    taking all of this into account, if we had a team named PandaBlitz,
    had the team number #994, and was located at הכפר הירוק, then the 
    function would return: {994:{"PandaBlitz":"הכפר הירוק"}}
    """

    team_number = -1
    
    while team_number != 0:
        # team number!
        temp_team_number = input("\nEnter Team Number. Do not Use Hashtags(#). for example, team number #7543's input would be 7543\n")
        try:
            temp_team_number = int(temp_team_number)
            pass  
        except ValueError:
            print("\nPlease try again and enter a number, for the team number. make sure to not use Hashtags")
            continue
        if temp_team_number == 0:
            break
        team_number = temp_team_number

        # team name!
        print(f"\nTeam #{team_number}'s number added to database. make sure to follow the next steps, or else the team wont be saved.")
        temp_team_name = input("\nEnter Team name. for exaample, if the team name was Giraffes, write \"giraffes\". writing in hebrew can be done normally.\n")
        team_name = flip_hebrew(temp_team_name)
        print(f"\nTeam {team_number}'s name({team_name}) has been added to the database.")

        # team location!
        temp_team_place = input("\nEnter Team location. for exaample, if the team was from הוד השרון and from הירוק school,\nit will look like this: \"בית הספר הירוק, הוד השרון\"\n")
        team_place = flip_hebrew(temp_team_place)
        print(f"(\nTeam {team_number}'s name({team_name}) has been added to the database.")
        teams.update({team_number : {team_name:team_place}})
    if save == False:
        return teams
    else:
        save_data("data.txt", teams)
        return teams

def save_data(file , thing):
    with open(file, 'w') as file:
        json.dump(thing, file, indent=4)
def get_data(file):
    with open('data.txt', 'r') as file:
        return json.load(file)

def team_list(data = get_data("data.txt")):
    for i in range(len(data)):
        num = get_team_numbers(data)[i]
        print(f"#{get_team_numbers(data)[0]} {team_name(data, num)} - {team_location(data, num)}")
#Generate the teams

# hi = add_teams(teams = get_data("data.txt"), save=True)
team_list()
