import pandas as pd

# DATAFRAME IS TABULAR DATA STRUCTURE WITH ROWS AND COLUMNS(2D)

data =  {
        "Name": ["Motu", "Patlu", "Ghasita"],
        "Age": [50, 60, 22]
        }

df = pd.DataFrame(data, index = ['Employee 1', 'Employee 2', 'Employee 3'])

# print(df)

# print(df.loc['Employee 3'])

# print(df.iloc[2])

# ADD A NEW COLUMN
df["Position"] = ["samosa", "chiya", "churot"]

# ADD A NEW ROW
new_rows = pd.DataFrame([{"Name": "Jhatka", "Age": 12, "Position": "science"},
                         {"Name": "Chingum", "Age": 42, "Position": "Police"}],
                        index = ["Employee 4", "Employee 5"])

df = pd.concat([df,new_rows])


print(df)
