from sportsreference.nba.schedule import Schedule
import pandas as pd
from datetime import datetime

def color_negative_values(val):
  color = 'red' if val =="Loss" else 'white'
  return 'color: %s' % color

portland_schedule = Schedule('POR')
i = 0
rows = []
for game in portland_schedule:
    source = portland_schedule.dataframe
    if source.wins[i] is not None:
        rows.append([game.game, game.date, game.result, game.streak, game.wins, game.game - game.wins])
    i += 1
df = pd.DataFrame(rows, columns=["game", "date", "result", "streak", "wins", "losses"])
df.set_index(['game'])


df.set_index(['game']).style.applymap(color_negative_values).set_caption("Trail Blazers Games").background_gradient(cmap='coolwarm', subset='wins')
df.wins
# # json = df.to_json() 
# # print(json) 

# from sportsipy.nba.boxscore import Boxscores

# # Pulls all games between and including January 1, 2018 and January 5, 2018
# games = Boxscores(datetime(2021, 2, 15))
# # Prints a dictionary of all results from January 1, 2018 and January 5,
# # 2018
# print(games.games)