import pandas as pd


# Data cleaning = process of fixing/removing:
#                 incomplete, incorrect, or irrelevant data.

df = pd.read_csv("file.csv")

# 1. Drop irrelevant columns
# df = df.drop(columns=["Legendary", "No"])

# 2. Handle missing data
# df = df.dropna(subset=["Type2"])
# df = df.fillna({"Type2" : "NONE"})

# 3. Fix inconsistent values
# df["Type1"] = df["Type1"].replace({"Grass":"GRASS",
#                                    "Water":"WATER"})

# 4. Standardize Text
# df["Name"] = df["Name"].str.lower()

# 5. Fix data types

# df["Legendary"] = df["Legendary"].astype(bool)

# 6. Delete duplicates

df = df.drop_duplicates()



print(df.to_string())