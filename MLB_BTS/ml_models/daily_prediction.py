import pandas as pd
import numpy as np
import time
import datetime
import statsapi
from MLB_BTS.statsapi_utils.team_player_data import PlayerTeamInformation 



for dates in ["03/26/2019","03/27/2019","03/28/2019","04/09/2019"]:

    pti = PlayerTeamInformation()
    trial = pti.scheduled_games(dates)

    if len(trial) == 0:
        continue
    else:
        print(trial)

def final_stats_data(season_start_date,date,season):

    start = time.time()
    game_ids = pti.scheduled_games(date)
    team_roster = pti.team_roster(game_ids)
    player_ids = pti.player_id_lookup(team_roster,season=season)
    player_stats = pti.player_basic_stats(player_ids,season_start_date,(pd.to_datetime(date) - datetime.timedelta(1)).strftime("%m/%d/%Y"))
    player_stats['got_hit'] = pti.player_got_hit(player_stats.Player_id,date)
    player_stats_final = player_stats[player_stats.got_hit.notnull()]
    end = time.time()

    print("Time elapsed:", end-start)

    return player_stats_final





final_data = final_stats_data('03/28/2019','04/19/2019',2019)




game_date = "04/19/2019"
stats_hydration = f'stats(group=[hitting],type=[byDateRange],startDate={game_date},endDate={game_date},sportId=1)'
get_player_stats = statsapi.get('person', {'personId': 502481, 'hydrate': stats_hydration})

565130
params = {'gamePk':565130,
  'fields': 'gameData,teams,teamName,shortName,teamStats,batting,atBats,runs,hits,rbi,strikeOuts,baseOnBalls,leftOnBase,players,boxscoreName,liveData,boxscore,teams,players,id,fullName,batting,avg,ops,era,battingOrder,info,title,fieldList,note,label,value'}
r = statsapi.get('game', params)
stats_game = r['liveData']['boxscore']['teams']['away']['players'].get('ID' + str(502481), False)
