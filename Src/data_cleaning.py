import pandas as pd
import numpy as np
import os

df = pd.read_excel(r"C:\Users\RIGVED UMESH\OneDrive\Desktop\AxionRay_Assignment_Hridya\Data\DA -Task 2..xlsx")
df = df.drop_duplicates()
num_cols =  df.select_dtypes(include=['int64', 'float64']).columns
df[num_cols] = df[num_cols].apply(lambda x: x.fillna(x.median()))
cat_cols = df.select_dtypes(include=['object']).columns
df[cat_cols] = df[cat_cols].apply(lambda x: x.fillna(x.mode()[0]))


for col in cat_cols:
    df[col] = df[col].astype(str).str.strip().str.capitalize()

for col in num_cols:
    df[col] = pd.to_numeric(df[col], errors='coerce')
    df[num_cols] = df[num_cols].apply(lambda x: x.fillna(x.median()))
for col in num_cols:
    lower = df[col].quantile(0.05)
    upper = df[col].quantile(0.95)
    df[col] = df[col].clip(lower, upper)


df.to_excel(r"C:\Users\RIGVED UMESH\OneDrive\Desktop\AxionRay_Assignment_Hridya\Data\task2_cleaned.xlsx", index=False)
print('data cleaning completed. cleaned file saved!')

