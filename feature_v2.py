# feature_v2.py
import pandas as pd

df = pd.read_csv("A:\TERM 4\CAB214\CA2\house_data.csv")

if 'sqft_living' in df.columns:
    df['log_sqft'] = df['sqft_living'].apply(lambda x: x+1)

print(df.head())