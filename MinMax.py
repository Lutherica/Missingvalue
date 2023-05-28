import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.impute import SimpleImputer

csv_data = pd.read_csv('shopping_data_missingvalue.csv')
array = csv_data.values

x = array[:, 2:5] # ambil kolom kedua sampai kelima
y = array[:, 0:1] # ambil kolom pertama sampai kedua

print(csv_data)
print(x)

imputer = SimpleImputer(missing_values=np.nan, strategy='mean') # Menggunakan rata-rata untuk mengisi nilai yang hilang
imputed_x = imputer.fit_transform(x)

dataset = pd.DataFrame({'Customer Data': array[:, 0], 'Gender': array[:, 1], 'Age': imputed_x[:, 0],
                       'Income': imputed_x[:, 1], 'Spending Score': imputed_x[:, 2]})
print('dataset sebelum normalisasi:')
print(dataset)

minMax = preprocessing.MinMaxScaler(feature_range=(0, 1))
data = minMax.fit_transform(imputed_x)
dataset_normalized = pd.DataFrame({'Age': data[:, 0], 'Income': data[:, 1], 'Spending Score': data[:, 2]})
print('dataset setelah normalisasi:')
print(dataset_normalized)
