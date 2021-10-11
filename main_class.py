import pandas as pd
from scipy.spatial.distance import cosine
from random import randint as rnd
import string



class Mainclass:
    def __init__(self):
        self.targ_vec = []
        self.sp_df = pd.read_csv('dialog_data.csv')
        self.alf = string.ascii_lowercase
        self.di = self.create_di()

    def create_di(self):
        di = {}
        for i in range(26):
            di[self.alf[i]] = i
        return di