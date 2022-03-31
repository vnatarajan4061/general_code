import pandas as pd
import numpy as np
import datetime
import statsapi
from MLB_BTS.statsapi_utils.team_player_data import player_team_information



for dates in ["03/26/2019","03/27/2019","03/28/2019","04/09/2019"]:

    trial = player_team_info.scheduled_games(dates)

    if len(trial) == 0:
        continue
    else:
        print(trial)

print(%%timeit)


def final_stats_data(season_start_date,date,season):

    %%timeit
    player_team_info = player_team_information()
    game_ids = player_team_info.scheduled_games(date)
    team_roster = player_team_info.team_roster(game_ids)
    player_ids = player_team_info.player_id_lookup(team_roster,season=season)
    player_stats = player_team_info.player_basic_stats(player_ids,season_start_date,(pd.to_datetime(date) - datetime.timedelta(1)).strftime("%m/%d/%Y"))
    player_stats['got_hit'] = player_team_info.player_got_hit(player_stats.Player_id,date)
    player_stats_final = player_stats[player_stats.got_hit.notnull()]

    return player_stats_final


final_stats_data('03/28/2019','04/19/2019',2019)

game_date = "04/19/2019"
stats_hydration = f'stats(group=[hitting],type=[byDateRange],startDate={game_date},endDate={game_date},sportId=1)'
get_player_stats = statsapi.get('person', {'personId': 502481, 'hydrate': stats_hydration})

565130
params = {'gamePk':565130,
  'fields': 'gameData,teams,teamName,shortName,teamStats,batting,atBats,runs,hits,rbi,strikeOuts,baseOnBalls,leftOnBase,players,boxscoreName,liveData,boxscore,teams,players,id,fullName,batting,avg,ops,era,battingOrder,info,title,fieldList,note,label,value'}
r = statsapi.get('game', params)
stats_game = r['liveData']['boxscore']['teams']['away']['players'].get('ID' + str(502481), False)
