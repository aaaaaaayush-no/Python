import matplotlib.pyplot as plt
import numpy as np

# grid()

x = [1,2,3,4,5]
y = [5, 10, 15, 20, 25]

plt.plot(x,y)

plt.grid(axis = "y", 
         linewidth = 3,
         color = "lightgray",
         linestyle = "dashed")

plt.show()