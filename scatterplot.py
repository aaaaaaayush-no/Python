import matplotlib.pyplot as plt
import numpy as np


x1 = np.array([1,2,3,2,5,6,7])
y1 = np.array([60, 70, 70, 75, 83, 95, 98])

x2 = np.array([0,1,2,5,2,6,7])
y2 = np.array([12, 23, 54, 66, 78, 91, 95])

plt.scatter(x1,y1, color = "blue",
            alpha = 0.5,
            s = 100, 
            label = "Class A")

plt.scatter(x2,y2, color = "lightblue",
            alpha = 0.5,
            s = 100, label = "Class B")

plt.xlabel("Hours")
plt.ylabel("Marks")

plt.legend()

plt.show()