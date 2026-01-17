import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv("file.csv")

type_count = df["Type1"].value_counts(ascending = True)

plt.barh(type_count.index,type_count.values, color = "Blue")

plt.xlabel("No. of pokemons", size = 20)
plt.ylabel("Pokemon types", size = 20)

plt.tight_layout()
plt.show()



