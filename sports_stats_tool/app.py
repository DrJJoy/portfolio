"""
Basketball Stats Tool Project

Build a console-based basketball team statistics tool
to help you divide up a group of players into teams and then provide a team analysis.

March 21, 2022
Second Python Project
"""

from constants import TEAMS, PLAYERS
import copy

teams = copy.deepcopy(TEAMS)
players = copy.deepcopy(PLAYERS)

def start():
    print("Basketball Team Stats Tool")
    print("----MENU----")
    print("Here are your choices:")
    print("1: Display Team Stats")
    print("2: Quit")

def first_menu():
    selection = input("Enter An Option:  ")
    if (selection == "1"):
        #print(teams_with_players[])
        #I also want each of the teams with players to be a choice
        print("Teams to view:")
        print(f'''
        1) {TEAMS[0]}   
        2) {TEAMS[1]}
        3) {TEAMS[2]}''')
        select_team()
    elif(selection == "2"):
        print("Have a nice day!")
    else:
        print("Please select 1 or 2.")

def clean_constants():
    for player in players:
        player["height"] = player['height'].split()
        player['height'] = int(player['height'][0])
        player['guardians'] = player['guardians'].split(" and ")
        if player['experience'] == 'YES':
            player['experience'] = True
        else:
            player['experience'] = False
    return players, teams


def assign_players(players,teams):
    Panthers = []
    Bandits = []
    Warriors = []
       
    players_lists = [Panthers, Bandits, Warriors]
    
    num_teams = len(teams)
    for num in range(len(players)):
        players_lists[num % num_teams].append(players[num])
    
    return Panthers, Bandits, Warriors, players
    
      
def select_team():
    choice = input("Please select a team from the list:")
    if choice == '1':
        display_stats(Panthers, "Panthers")
    elif choice == '2':
        display_stats(Bandits, "Bandits")
    elif choice == '3':
        display_stats(Warriors, "Warriors")
    else:
        print("Please choose 1, 2 or 3")

        

def display_stats(team, team_name):  
    while True:
        players_on_team = [player['name'] for player in team]
        average_height = round(sum([player["height"] for player in team]) / len(players_on_team), 2)
        num_experienced = len([player for player in team if player['experience'] == True])
        num_inexperienced = len([player for player in team if player['experience'] == False])
        guardians = [", ".join(player['guardians']) for player in team]
              
        print("\n", "TEAM: {} Stats".format(team_name))
        print("-" * 20, "\n")
        print("Players on Team: ", end="")
        print(", ".join(players_on_team))
        print("\n", "Total Players: {}".format(len(team)))
        print("Average height: ",average_height)
        print(f"Experienced Players: {num_experienced}")
        print(f"Inexperienced Players: {num_inexperienced}")
        print("\n", "Guardians:")
        print(", ".join(guardians))
        break

if __name__ == "__main__":
    Panthers, Bandits, Warriors, teams_list = assign_players(*clean_constants())
    start()
    first_menu()
           

