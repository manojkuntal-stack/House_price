import pandas as pd

df = pd.read_csv("A:\TERM 4\CAB214\CA2\house_data.csv")

# Better missing handling
df.fillna(method='ffill', inplace=True)

# Encoding categorical
df = pd.get_dummies(df, drop_first=True)

print(df.head())