import pandas as pd


df = pd.read_excel(r"C:\Users\RIGVED UMESH\OneDrive\Desktop\AxionRay_Assignment_Hridya\Data\DA -Task 2..xlsx")
# print(df.head())
# print("Columns & Data types:/n", df.dtypes)




for col in df.columns:
    print(f"\nColumn: {col}")
    print(f"Data Type: {df[col].dtype}")
    print(f"Unique Values: {df[col].unique()}")
    if df[col].dtype in ['int64' , 'float64']:
        print(f"Min: {df[col].min()}")
        print(f"Max: {df[col].max()}")
        print(f"Mean: {df[col].mean():.2f}")
        print(f"Meadian: {df[col].median():.2f}")
    else:
        print(f"Top Values:\n {df[col].value_counts().head(5)}")
    




