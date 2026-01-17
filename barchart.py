import matplotlib.pyplot as plt
import numpy as np

category = np.array(["Grains", "Fruits", "Meat", "Vege"])
values = np.array([20, 30, 60, 10])

# plt.bar(category, values, color = "skyBlue")
plt.barh(category, values, color = "skyBlue")

plt.title("Items Consumption", size = 20)
plt.xlabel("Foods")
plt.ylabel("Quantity")


plt.show()