from sportsipy.nba.teams import Teams

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def get_height_in_inches(height):
    feet, inches = height.split('-')
    return int(feet) * 12 + int(inches)

def get_height_in_feet(height):
    feet = height - (height % 1)
    inches = 12 * (height % 1)
    return int(feet) * 12 + int(inches)

def get_height_in_feet(height):
    height = height / 12
    feet = round(height - (height % 1))
    inches = round(12 * (height % 1))
    return feet, inches

def print_players(team_heights):
    tallest_player = max(team_heights, key=team_heights.get)
    shortest_player = min(team_heights, key=team_heights.get)
    tallest_height = team_heights[tallest_player]
    shortest_height = team_heights[shortest_player]
    tallest_feet = get_height_in_feet(tallest_height)[0]
    tallest_inches = get_height_in_feet(tallest_height)[1]
    shortest_feet = get_height_in_feet(shortest_height)[0]
    shortest_inches = get_height_in_feet(shortest_height)[1]
    difference = tallest_height - shortest_height
    print('%s: %s\'%s\" & %s: %s\'%s\" for a difference of: %s in.' % (tallest_player, tallest_feet, tallest_inches, shortest_player, shortest_feet, shortest_inches, difference))
    return(tallest_player, shortest_player, tallest_feet, tallest_inches, shortest_feet, shortest_inches, difference)

def display_data():
    master_list = []
    for team in Teams():
        print('=' * 80)
        print(team.name)
        team_heights = {}
        for player in team.roster.players:
            height = get_height_in_inches(player.height)
            team_heights[player.name] = height
        height_diff = print_players(team_heights)
        master_list.append([team.name, height_diff])
    print(master_list)
    return master_list

master_list = [['Brooklyn Nets', ('DeAndre Jordan', 'Chris Chiozza', 6, 11, 5, 11, 12)], ['Los Angeles Clippers', ('Ivica Zubac', 'Lou Williams', 7, 0, 6, 1, 11)]]
# master_list = display_data()
master_list = [['Brooklyn Nets', ('DeAndre Jordan', 'Chris Chiozza', 6, 11, 5, 11, 12)], ['Los Angeles Clippers', ('Ivica Zubac', 'Lou Williams', 7, 0, 6, 1, 11)], ['Milwaukee Bucks', ('Brook Lopez', 'D.J. Augustin', 7, 0, 5, 11, 13)], ['Utah Jazz', ('Rudy Gobert', 'Donovan Mitchell', 7, 0, 6, 0, 12)], ['Philadelphia 76ers', ('Joel Embiid', 'Tyrese Maxey', 7, 0, 6, 2, 10)], ['Golden State Warriors', ('James Wiseman', 'Nico Mannion', 7, 0, 6, 2, 10)], ['Los Angeles Lakers', ('Marc Gasol', 'Quinn Cook', 6, 11, 6, 1, 10)], ['Dallas Mavericks', ('Boban Marjanović', 'Trey Burke', 7, 4, 6, 0, 16)], ['Indiana Pacers', ('Domantas Sabonis', 'Aaron Holiday', 6, 11, 6, 0, 11)], ['Charlotte Hornets', ('Nick Richards', 'Terry Rozier', 7, 0, 6, 1, 11)], ['Toronto Raptors', ('Aron Baynes', 'Kyle Lowry', 6, 10, 6, 0, 10)], ['Sacramento Kings', ('Hassan Whiteside', 'Kyle Guy', 7, 0, 6, 1, 11)], ['Atlanta Hawks', ('Clint Capela', 'Brandon Goodwin', 6, 10, 6, 0, 10)], ['New York Knicks', ('Mitchell Robinson', 'Jared Harper', 7, 0, 5, 10, 14)], ['Cleveland Cavaliers', ('JaVale McGee', 'Collin Sexton', 7, 0, 6, 1, 11)], ['Denver Nuggets', ('Bol Bol', 'Facundo Campazzo', 7, 2, 5, 10, 16)], ['Portland Trail Blazers', ('Harry Giles', 'Damian Lillard', 6, 11, 6, 2, 9)], ['San Antonio Spurs', ('Jakob Poeltl', 'Patty Mills', 7, 1, 6, 1, 12)], ['Chicago Bulls', ('Luke Kornet', 'Devon Dotson', 7, 2, 6, 2, 12)], ['Houston Rockets', ('DeMarcus Cousins', 'Eric Gordon', 6, 10, 6, 3, 7)], ['New Orleans Pelicans', ('Steven Adams', 'Eric Bledsoe', 6, 11, 6, 1, 10)], ['Detroit Pistons', ('Mason Plumlee', 'Saben Lee', 6, 11, 6, 2, 9)], ['Orlando Magic', ('Mo Bamba', 'Frank Mason III', 7, 0, 5, 11, 13)], ['Minnesota Timberwolves', ('Karl-Anthony Towns', 'Jordan McLaughlin', 6, 11, 5, 11, 12)], ['Phoenix Suns', ('Frank Kaminsky', 'Chris Paul', 7, 0, 6, 0, 12)], ['Miami Heat', ('Meyers Leonard', 'Kendrick Nunn', 7, 0, 6, 2, 10)], ['Boston Celtics', ('Tacko Fall', 'Tremont Waters', 7, 5, 5, 10, 19)], ['Washington Wizards', ('Robin Lopez', 'Ish Smith', 7, 0, 6, 0, 12)], ['Oklahoma City Thunder', ('Moses Brown', 'Luguentz Dort', 7, 2, 6, 3, 11)], ['Memphis Grizzlies', ('Jonas Valančiūnas', 'Tyus Jones', 6, 11, 6, 0, 11)]]
print(type(master_list))

difference_list = []
index_list = []
for team in master_list:
    index_list.append(team[0])
    difference_list.append(team[1][-1])

# set font
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = 'Helvetica'

# set the style of the axes and the text color
plt.rcParams['axes.edgecolor']='#333F4B'
plt.rcParams['axes.linewidth']=0.8
plt.rcParams['xtick.color']='#333F4B'
plt.rcParams['ytick.color']='#333F4B'
plt.rcParams['text.color']='#333F4B'

# create some fake data
print(difference_list)
percentages = pd.Series(difference_list, 
                        index=index_list)
df = pd.DataFrame({'percentage' : percentages})
df = df.sort_values(by='percentage')

# we first need a numeric placeholder for the y axis
my_range=list(range(1,len(df.index)+1))

fig, ax = plt.subplots(figsize=(5,10))

# create for each expense type an horizontal line that starts at x = 0 with the length 
# represented by the specific expense percentage value.
plt.hlines(y=my_range, xmin=0, xmax=df['percentage'], color='#007ACC', alpha=0.2, linewidth=5)

# create for each expense type a dot at the level of the expense percentage value
plt.plot(df['percentage'], my_range, "o", markersize=5, color='#007ACC', alpha=0.6)

# set labels
ax.set_xlabel('Height Difference', fontsize=15, fontweight='black', color = '#333F4B')
ax.set_ylabel('')

# set axis
ax.tick_params(axis='both', which='major', labelsize=12)
plt.yticks(my_range, df.index)

# add an horizonal label for the y axis 
fig.text(-0.23, 0.96, 'Team', fontsize=15, fontweight='black', color = '#333F4B')

# change the style of the axis spines
# ax.spines['top'].set_color('none')
# ax.spines['right'].set_color('none')
# ax.spines['left'].set_smart_bounds(True)
# ax.spines['bottom'].set_smart_bounds(True)

# set the spines position
ax.spines['bottom'].set_position(('axes', -0.04))
ax.spines['left'].set_position(('axes', 0.015))

plt.savefig('hist2.png', dpi=300, bbox_inches='tight')

"""
================================================================================
Brooklyn Nets
DeAndre Jordan: 6'11" & Chris Chiozza: 5'11" for a difference of: 12 in.
================================================================================
Los Angeles Clippers
Ivica Zubac: 7'0" & Lou Williams: 6'1" for a difference of: 11 in.
================================================================================
Milwaukee Bucks
Brook Lopez: 7'0" & D.J. Augustin: 5'11" for a difference of: 13 in.
================================================================================
Utah Jazz
Rudy Gobert: 7'0" & Donovan Mitchell: 6'0" for a difference of: 12 in.
================================================================================
Philadelphia 76ers
Joel Embiid: 7'0" & Tyrese Maxey: 6'2" for a difference of: 10 in.
================================================================================
Golden State Warriors
James Wiseman: 7'0" & Nico Mannion: 6'2" for a difference of: 10 in.
================================================================================
Los Angeles Lakers
Marc Gasol: 6'11" & Quinn Cook: 6'1" for a difference of: 10 in.
================================================================================
Dallas Mavericks
Boban Marjanović: 7'4" & Trey Burke: 6'0" for a difference of: 16 in.
================================================================================
Indiana Pacers
Domantas Sabonis: 6'11" & Aaron Holiday: 6'0" for a difference of: 11 in.
================================================================================
Charlotte Hornets
Nick Richards: 7'0" & Terry Rozier: 6'1" for a difference of: 11 in.
================================================================================
Toronto Raptors
Aron Baynes: 6'10" & Kyle Lowry: 6'0" for a difference of: 10 in.
================================================================================
Sacramento Kings
Hassan Whiteside: 7'0" & Kyle Guy: 6'1" for a difference of: 11 in.
================================================================================
Atlanta Hawks
Clint Capela: 6'10" & Brandon Goodwin: 6'0" for a difference of: 10 in.
================================================================================
New York Knicks
Mitchell Robinson: 7'0" & Jared Harper: 5'10" for a difference of: 14 in.
================================================================================
Cleveland Cavaliers
JaVale McGee: 7'0" & Collin Sexton: 6'1" for a difference of: 11 in.
================================================================================
Denver Nuggets
Bol Bol: 7'2" & Facundo Campazzo: 5'10" for a difference of: 16 in.
================================================================================
Portland Trail Blazers
Harry Giles: 6'11" & Damian Lillard: 6'2" for a difference of: 9 in.
================================================================================
San Antonio Spurs
Jakob Poeltl: 7'1" & Patty Mills: 6'1" for a difference of: 12 in.
================================================================================
Chicago Bulls
Luke Kornet: 7'2" & Devon Dotson: 6'2" for a difference of: 12 in.
================================================================================
Houston Rockets
DeMarcus Cousins: 6'10" & Eric Gordon: 6'3" for a difference of: 7 in.
================================================================================
New Orleans Pelicans
Steven Adams: 6'11" & Eric Bledsoe: 6'1" for a difference of: 10 in.
================================================================================
Detroit Pistons
Mason Plumlee: 6'11" & Saben Lee: 6'2" for a difference of: 9 in.
================================================================================
Orlando Magic
Mo Bamba: 7'0" & Frank Mason III: 5'11" for a difference of: 13 in.
================================================================================
Minnesota Timberwolves
Karl-Anthony Towns: 6'11" & Jordan McLaughlin: 5'11" for a difference of: 12 in.
================================================================================
Phoenix Suns
Frank Kaminsky: 7'0" & Chris Paul: 6'0" for a difference of: 12 in.
================================================================================
Miami Heat
Meyers Leonard: 7'0" & Kendrick Nunn: 6'2" for a difference of: 10 in.
================================================================================
Boston Celtics
Tacko Fall: 7'5" & Tremont Waters: 5'10" for a difference of: 19 in.
================================================================================
Washington Wizards
Robin Lopez: 7'0" & Ish Smith: 6'0" for a difference of: 12 in.
================================================================================
Oklahoma City Thunder
Moses Brown: 7'2" & Luguentz Dort: 6'3" for a difference of: 11 in.
================================================================================
Memphis Grizzlies
Jonas Valančiūnas: 6'11" & Tyus Jones: 6'0" for a difference of: 11 in.
"""
