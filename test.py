import csv
import pandas as pd

fileName = 'USvideos.csv'

df = pd.read_csv(fileName, index_col=0)

for col in df.columns:
    print(col)