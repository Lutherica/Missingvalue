import pandas as pd

df = pd.read_csv('shopping_data_missingvalue.csv')
df_mean = df.fillna(df.mean(numeric_only=True))

print('Data sebelum di proses:')
print(df)
print('Data setelah di isi dengan mean:')
print(df_mean)
