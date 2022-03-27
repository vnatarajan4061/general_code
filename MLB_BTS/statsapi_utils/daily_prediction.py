import pandas as pd
import numpy as np
import datetime
import statsapi
from MLB_BTS.team_player_data import player_team_information

stardate = "04/06/2019"
enddate = "04/06/2019"

stats_hydration = f'stats(group=[hitting],type=[byDateRange],startDate={stardate},endDate={enddate},sportId=1)'
get_player_stats = statsapi.get('person', {'personId': 547989, 'hydrate': stats_hydration})

get_player_stats

player_team_info = player_team_information()

team_id_data = player_team_info.team_id_lookup()
game_team_ids = player_team_info.scheduled_games("04/09/2019")
gameday_roster = player_team_info.team_roster(game_team_ids)

player_team_info.player_id_lookup(gameday_roster)
