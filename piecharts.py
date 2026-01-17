import matplotlib.pyplot as plt
import numpy as np


categories = ["1st", "2nd", "3rd", "4th"]
percen = np.array([200, 115, 335, 240])

colors = ["Red", "yellow", "blue", "green"]

plt.pie(percen, labels = categories, 
        autopct = "%1.1f%%",
        colors = colors,
        explode = [0,0,0,0.1],
        shadow = True, 
        startangle=90)

plt.title("FuckOff")

plt.show()