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

        self.main_season = [yr for yr in range(2005,datetime.datetime.now().year)]


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

        return team_id_data

    def team_roster(self):
        statsapi.roster()

    def player_id_lookup(self):
        statsapi.lookup_player()



if __name__ == 'team_player_data':
    player_team_information()
