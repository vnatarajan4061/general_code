import pandas as pd
import numpy as np
from xgboost import XgboostClassifier


# need to take a look at these columns to see why they may not want to be included in modeling
['airOuts', 'atBatsPerHomeRun', 'catchersInterference', 'groundIntoTriplePlay']
