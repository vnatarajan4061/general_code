import pandas as pd
import numpy as np
import datetime
import statsapi

class player_team_information:
    def __init__(self):
        self.team_list = ['diamondbacks','braves','orioles','red sox','cubs','white sox'
        ,'reds','guardians','rockies','tigers','astros','royals','angels','dodgers'
        ,'marlins','brewers','twins','mets','yankees','athletics','phillies','pirates'
        ,'padres','giants','mariners','cardinals','rays','rangers','blue jays','nationals']

        self.main_season = [yr for yr in range(2019,datetime.datetime.now().year) if yr != 2020]

    # Only run this function once a year to get the ids for each team
    def team_id_lookup(self):

        team_id_data = pd.DataFrame()
        table_id = 1
        for tm in self.team_list:
            for yr in self.main_season:
                if tm == 'guardians' and yr <= 2021:
                    id_data = statsapi.lookup_team('indians', season=yr)
                    team_id_data = team_id_data.append({'id':table_id,'Team':tm,'Year':yr,'Team_id':id_data[0]['id']},ignore_index=True)

                    table_id += 1
                else:
                    id_data = statsapi.lookup_team(tm, season=yr)
                    team_id_data = team_id_data.append({'id':table_id,'Team':tm,'Year':yr,'Team_id':id_data[0]['id']},ignore_index=True)

                    table_id += 1

        team_id_data.Team_id = team_id_data.Team_id.astype(int)

        return team_id_data

##### Will need a function to get the games on that date so we can get rid of the try pass below

    def scheduled_games(self, game_date):
        game_list = statsapi.schedule(date=game_date)

        team_game_ids = {}
        for game in game_list:
            if game['game_type'] == 'R':
                team_game_ids[game['away_id']] = game_date
                team_game_ids[game['home_id']] = game_date

        return team_game_ids

    def team_roster(self, team_game_ids):
        tm_id_list, season_list, date_list, player_name_list = [],[],[],[]
        for tm_id, game_date in team_game_ids.items():
            roster = statsapi.roster(tm_id, date=game_date)
            roster_list = roster.split("\n")[:-1]
            for player in roster_list:
                player_position = player.split()[1]
                if player_position != 'P':
                    player_name_list.append(" ".join(player.split()[2:]))
                    tm_id_list.append(tm_id)
                    season_list.append(pd.to_datetime(game_date).year)
                    date_list.append(pd.to_datetime(game_date))

        roster_df = pd.DataFrame({'Team_id':tm_id_list,'Season':season_list,'Gameday_date':date_list,'Roster':player_name_list})

        return roster_df

    def player_id_lookup(self, roster_data):
        player_id_list = []
        for name in roster_data.Roster:
            player_id = statsapi.lookup_player(name, season=roster_data.Season.unique()[0])

            player_id_list.append(player_id[0]['id'])

        roster_data['Player_id'] = player_id_list

        return roster_data

    def player_stats(self, roster_player_data, season_start_date, time_period_final_date):
        stats_data = pd.DataFrame()
        for playerid in roster_player_data.Player_id:
            stats_hydration = f'stats(group=[hitting],type=[byDateRange],startDate={season_start_date},endDate={time_period_final_date},sportId=1)'
            get_player_stats = statsapi.get('person', {'personId': playerid, 'hydrate': stats_hydration})
            stats = get_player_stats['people'][0]['stats'][0]['splits'][0]['stat']

            stats_data = stats_data.append(stats, ignore_index=True)

        player_stats_data = roster_player_data.merge(stats_data, left_index=True, right_index=True, how='inner')

        return player_stats_data


if __name__ == 'team_player_data':
    player_team_information()
