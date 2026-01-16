import pandas as pd

df = pd.read_csv("file.csv", index_col = "Name")

#   SELECTION BY COLUMN

# print(df["Name"]. to_string())
# print(df["Code"].to_string())
# print(df[["Code", "Symbol"]]. to_string())

# SELECTION BY ROWS

# print(df.loc["Albanian lek":"Netherlands Antillean gu", ["Symbol"]])

# print(df.iloc[0:11:2, 0:2])

money = input('Enter the currency: ')

try:
    print(df.loc[money])

except KeyError:
    print(f"{money} not found")
