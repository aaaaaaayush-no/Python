import matplotlib.pyplot as plt
import numpy as np


scores = np.random.normal(loc=80, scale=10, size=100)

scores = np.clip(scores, 0, 100)

plt.hist(scores, bins = 10,
                 color="lightGreen",
                 edgecolor = "black")
plt.title("Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("No. of Students")

plt.show()