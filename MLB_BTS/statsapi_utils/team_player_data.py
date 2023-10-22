import pandas as pd
import numpy as np
import datetime
import statsapi

class PlayerTeamInformation:
    def __init__(self):
        self.team_list = ['diamondbacks','braves','orioles','red sox','cubs','white sox'
        ,'reds','guardians','rockies','tigers','astros','royals','angels','dodgers'
        ,'marlins','brewers','twins','mets','yankees','athletics','phillies','pirates'
        ,'padres','giants','mariners','cardinals','rays','rangers','blue jays','nationals']

        self.main_season = [yr for yr in range(2019,datetime.datetime.now().year) if yr != 2020]

    # Only run this function once a year to get the ids for each team
    # Do I even need this function?
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

    def player_id_lookup(self, roster_data, season):
        player_id_list = [statsapi.lookup_player(name,season=season)[0]['id'] for name in roster_data.Roster]
        # for name in roster_data.Roster:
        #     player_id = statsapi.lookup_player(name, season=season)
        #
        #     player_id_list.append(player_id[0]['id'])

        roster_data['Player_id'] = player_id_list

        return roster_data

    def player_basic_stats(self, roster_player_data, season_start_date, time_period_final_date):
        stats_data = pd.DataFrame()
        for playerid in roster_player_data.Player_id:
            stats_hydration = f'stats(group=[hitting],type=[byDateRange],startDate={season_start_date},endDate={time_period_final_date},sportId=1)'
            get_player_stats = statsapi.get('person', {'personId': playerid, 'hydrate': stats_hydration})

            if len(get_player_stats['people'][0]['stats'][0]['splits']) == 0:
                continue
            else:
                stats = get_player_stats['people'][0]['stats'][0]['splits'][0]['stat']

            stats['Player_id'] = playerid

            stats_data = stats_data.append(stats, ignore_index=True)

        player_stats_data = roster_player_data.merge(stats_data, left_on = 'Player_id', right_on= 'Player_id', how='inner')

        return player_stats_data

    def player_got_hit(self, player_id_list, game_date):
        hit_list = []
        for playerid in player_id_list:
            stats_hydration = f'stats(group=[hitting],type=[byDateRange],startDate={game_date},endDate={game_date},sportId=1)'
            get_player_stats = statsapi.get('person', {'personId': playerid, 'hydrate': stats_hydration})

            if len(get_player_stats['people'][0]['stats'][0]['splits']) == 0:
                hit_list.append(np.nan)
                continue
            else:
                number_of_hits = get_player_stats['people'][0]['stats'][0]['splits'][0]['stat']['hits']

                if number_of_hits > 0:
                    hit_list.append(True)
                else:
                    hit_list.append(False)

        return hit_list


if __name__ == 'team_player_data':
    PlayerTeamInformation()
