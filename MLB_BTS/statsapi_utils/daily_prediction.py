import pandas as pd
import numpy as np
import datetime
import statsapi
from MLB_BTS.statsapi_utils.team_player_data import player_team_information

player_team_info = player_team_information()

team_id_data = player_team_info.team_id_lookup()
game_team_ids = player_team_info.scheduled_games("04/09/2019")
gameday_roster = player_team_info.team_roster(game_team_ids)

gameday_player_id = player_team_info.player_id_lookup(gameday_roster)

stardate = "04/01/2019"
enddate = "04/19/2019"
stats_data = pd.DataFrame()
for playerid in gameday_player_id.Player_id:
    stats_hydration = f'stats(group=[hitting],type=[byDateRange],startDate={stardate},endDate={enddate},sportId=1)'
    get_player_stats = statsapi.get('person', {'personId': playerid, 'hydrate': stats_hydration})
    stats = get_player_stats['people'][0]['stats'][0]['splits'][0]['stat']

    stats_data = stats_data.append(stats, ignore_index=True)

column_list = ['gamesPlayed','groundOuts','runs','doubles','triples','homeRuns','strikeOuts',
'baseOnBalls','intentionalWalks','hits','hitByPitch','avg','atBats','obp','slg','ops','caughtStealing',
'stolenBases','stolenBasePercentage','groundIntoDoublePlay','numberOfPitches','plateAppearances',
'totalBases','rbi','leftOnBase','sacBunts','sacFlies','babip','groundOutsToAirouts']

[col for col in stats_data.columns if col not in column_list]

gameday_player_id.merge(stats_data, left_index=True, right_index=True, how='inner')

stats_data[['airOuts', 'atBatsPerHomeRun', 'catchersInterference', 'groundIntoTriplePlay']]
