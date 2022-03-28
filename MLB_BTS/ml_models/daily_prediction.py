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
