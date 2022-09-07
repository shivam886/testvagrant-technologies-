import pandas as pd
df = pd.read_excel('Book1.xlsx')
ma =  df['GST in %']
val = ma.max(axis=0)
m = df['GST in %'] == val
df_n = pd.DataFrame(df[m])
print(df_n['Product'])