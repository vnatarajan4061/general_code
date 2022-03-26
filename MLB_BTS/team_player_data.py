import pandas as pd
import numpy as np
import datetime
import statsapi


class player_team_information:
    def __init__(self):
        pass

    def team_id_lookup(self):
        statsapi.lookup_team()

    def team_roster(self):
        statsapi.roster()

    def player_id_lookup(self):
        statsapi.lookup_player()
