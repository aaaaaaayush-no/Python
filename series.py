import pandas as pd

#series = 1-dimensional labeled array that can hold data type

# data = [100, 102, 104, 200, 202]

# series = pd.Series(data, index = ['a', 'b', 'c', 'd', 'e'])

# series.loc["c"] = 200

# print(series.iloc[2])

# print(series[series<=200])

# print(series.loc["c"])


calories = {"Day 1": 1750, "Day 2": 2200, "Day 3": 1700}

series = pd.Series(calories)

# series.loc["Day 3"] += 200



print(series[series<2000])