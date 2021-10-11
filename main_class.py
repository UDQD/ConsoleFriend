import pandas as pd
from scipy.spatial.distance import cosine
from random import randint as rnd
import string



class Mainclass:
    def __init__(self):
        self.targ_vec = [1,1,1]
        self.sp_df = pd.read_csv('dialog_data.csv')
        self.alf = string.ascii_lowercase
        self.di = self.create_di()

    def create_di(self):
        di = {}
        for i in range(26):
            di[self.alf[i]] = i
        return di

    def get_vertex(self, s):

        s = s.lower()
        new_s = ''
        for c in s:
            if c in self.alf:
                new_s += c
        m = [0] * 26
        for e in new_s:
            m[self.di[e]] += 1
        return m

    def cust_cos(self, m):
        return cosine(self.targ_vec, m)

    def response(self, s):
        self.targ_vec = self.get_vertex(s)
        self.sp_df['dist'] = self.sp_df['Line_vec'].apply(self.cust_cos)

        resp = self.sp_df[self.sp_df['dist'] == self.sp_df['dist'].min()]
        x = rnd(0, len(resp) - 1)

        return resp.iloc[x]['Line_2']