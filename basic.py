import matplotlib.pyplot as plt
import numpy as np

x = np.array([2023, 2024, 2025, 2026])
y1 = np.array([15, 25, 30, 20])
y2 = np.array([17, 24, 39, 12])
y3 = np.array([10, 24, 46, 32])

line_style = dict(marker=".",
                  markersize = 10,
                  markerfacecolor = "blue",
                  markeredgecolor = "blue",
                  linestyle = "solid",
                  linewidth = 3
                  )

plt.plot(x, y1, color = "yellow", **line_style)

plt.plot(x, y2, color = "Green", **line_style)
plt.plot(x, y3, color = "Red", **line_style)
plt.show()