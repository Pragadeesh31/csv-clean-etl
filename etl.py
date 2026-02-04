import pandas as pd

df = pd.read_csv("PROJECT_DATA_11.csv")
# print(df)
# print("----------------------------------------------")
df = df.drop_duplicates()
# print(df)
# print("----------------------------------------------")


df["mark1"] = df["mark1"].fillna(0)
df["mark2"] = df["mark2"].fillna(0)
df["mark3"] = df["mark3"].fillna(0)
df["basis"] = df["basis"].fillna("NA")
# print(df.to_string())
# print("----------------------------------------------")

df["mark1"] = df["mark1"].astype(int)
df["mark2"] = df["mark2"].astype(int)
df["mark3"] = df["mark3"].astype(int)
# print(df.to_string())
# print("----------------------------------------------")

df = df.drop(columns=["Unnamed: 6"])

df["name"] = df["name"].str.title()
df["basis"] = df["basis"].str.upper()
print(df.to_string())
print("----------------------------------------------")

from sqlalchemy import create_engine

engine = create_engine(
    "postgresql+psycopg2://postgres:Praga3124@localhost:5432/project1"
)

df.to_sql(
    name="students",
    con=engine,
    if_exists="append",
    index=False
)

print("Data loaded successfully")
