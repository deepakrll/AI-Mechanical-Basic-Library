import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Temperature": [45, 50, 55, 60, 65],
    "Vibration": [0.5, 0.7, 1.0, 1.3, 1.7],
    "Failure": [0, 0, 1, 1, 1]
}

df = pd.DataFrame(data)
print(df.head())


plt.scatter(df["Temperature"], df["Vibration"], c=df["Failure"], cmap='coolwarm')
plt.xlabel("Temperature")
plt.ylabel("Vibration")
plt.title("Failure Analysis")
plt.show()
