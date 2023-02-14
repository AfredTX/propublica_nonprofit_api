import pandas as pd
import os


df = pd.read_csv(fr'{os.getcwd()}\nonprofit_explorer.csv')

df = df[(df['city'] == 'BALTIMORE') & (df['state'] == 'MD')]

applicable_ntee_codes = ['B', 'F', 'I', 'J', 'L', 'O', 'P', 'S', 'T']

df['ntee_cat'] = df['ntee_code'].str[0]

df = df[df['ntee_cat'].isin(applicable_ntee_codes)]



print(df.info())