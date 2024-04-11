import pandas as pd
import numpy as np


df_wine = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data', header=None)
df_wine.columns = ['Class lael', 'Alcohol', 'Malic acid', 'Ash', 'Alcalinity of ash', 'Magnesium',
                   'Total phenols', 'Flavvanoids', 'Nonflavanoid phenols', 'Proanthocyanins',
                   'Color intensity', 'Hue', 'OD280/OD315 of diluted wines', 'Proline']

# print(df_wine)

X = df_wine.iloc[ : , :2].values
Y = df_wine.iloc[ : , 0].values

X_pd = pd.DataFrame(X)
Y_pd = pd.DataFrame(Y)

print(X_pd, Y_pd)


# mms = MinMaxScaler() # [0,1] 범위로 스케일링
# stdsc = StandardScaler() # mean값이 0으로 스케일링