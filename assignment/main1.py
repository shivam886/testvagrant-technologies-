from re import A
import pandas as pd
df = pd.read_excel('Book1.xlsx')
tot =  df['Unit price in Rupees']
print(tot.sum(axis=0))