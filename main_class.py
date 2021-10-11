import pandas as pd
from scipy.spatial.distance import cosine
from random import randint as rnd
import string
from ast import literal_eval



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

    def low_dim(self, m):
        m = literal_eval(m)
        return m

    def response(self, s):
        self.targ_vec = self.get_vertex(s)
        self.sp_df['Line_vec'] = self.sp_df['Line_vec'].apply(self.low_dim)
        self.sp_df['dist'] = self.sp_df['Line_vec'].apply(self.cust_cos)

        resp = self.sp_df[self.sp_df['dist'] == self.sp_df['dist'].min()]
        x = rnd(0, len(resp) - 1)

        return resp.iloc[x]['Line_2']



    def censor(self, s):
        bad_words = [self.alf[1] + self.alf[8] + self.alf[19] + self.alf[2] + self.alf[7],
                     self.alf[5] + self.alf[20] + self.alf[2] + self.alf[10],
                     self.alf[22] + self.alf[7] + self.alf[14] + self.alf[17] + self.alf[4],
                     self.alf[0] + self.alf[18] + self.alf[18],
                     self.alf[13] + self.alf[8] + self.alf[6] + self.alf[6]]
        for el in bad_words:
            if el in s:
                l = len(el)
                for i in range(len(s) - l + 1):
                    if s[i:i + l] == el:
                        s = s[:i + 1] + '*' * (l - 2) + s[i + l - 1:]
        return s