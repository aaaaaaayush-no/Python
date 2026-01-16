import matplotlib.pyplot as plt
import numpy as np

x = np.array([2023, 2024, 2025, 2026])
y1 = np.array([15, 25, 30, 20])
y2 = np.array([17, 24, 39, 12])
y3 = np.array([10, 8, 16, 32])

plt.title("Class size", fontsize = 22,
                        family = "sans-serif",
                        fontweight = "bold",
                        color = "Purple")

plt.xlabel("year", fontsize = 10,
                    family="sans-serif",
                    color = "Gray")

plt.ylabel("No. of Students", fontsize = 10,
                    family="sans-serif",
                    color = "Gray")

plt.tick_params(axis="both", colors="gray")

plt.plot(x, y1)
plt.plot(x, y2)
plt.plot(x, y3)

plt.xticks(x)

plt.show()