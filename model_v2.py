# model_v2.py
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import pandas as pd

df = pd.read_csv("A:\TERM 4\CAB214\CA2\house_data.csv")
df = df.select_dtypes(include=['number']).dropna()

X = df.drop('price', axis=1)
y = df['price']

X_train, X_test, y_train, y_test = train_test_split(X, y)

model = RandomForestRegressor()
model.fit(X_train, y_train)

print("Improved model trained")