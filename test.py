import pandas as pd

first = pd.Series([10, 12, 14, 18], index=['f', 's','t', 'r'])
second = pd.Series([20, 24, 32, 56], index = ['f', 's', 't', 'r'])
df_s = pd.DataFrame({'f': [20], 's': [24], 't': [32], 'r': [56]}, index = ['BB'])
df_f = pd.DataFrame({'f': [10], 's': [12], 't': [14], 'r': [18]}, index = ['Tr'])
df = pd.DataFrame()
df = pd.concat([df, df_s, df_f], axis = 1)
print(df)
# df = pd.concat([df, df_f, df_s])
# print(df)
