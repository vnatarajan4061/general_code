import pandas as pd
import numpy as np
from MLB_BTS.statsapi_utils.team_player_data import player_team_information


class loading_data:
    def __init__(self):
        self.seasons_info = {'Seasons':[
                            {'Season':2019,'Start_Date':"03/28/2019","End_Date":"09/30/2019"},
                            {'Season':2021,'Start_Date':"04/01/2021","End_Date":"10/05/2021"}]}
        self.player_team_info = player_team_information()

    def base_stats(self):
        for season in self.seasons_info['Seasons']:
            for dates in season['Start_Date']
            self.player_team_info.scheduled_games()



if __name__ == "main":
    loading_data()
