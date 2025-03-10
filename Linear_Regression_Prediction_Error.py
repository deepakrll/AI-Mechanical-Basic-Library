import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

data = {
    "Vibration": [0.1, 0.3, 0.5, 0.7, 1.0, 1.2, 1.5, 1.8],
    "Wear_Level": [5, 15, 25, 35, 50, 65, 80, 95]
}
df = pd.DataFrame(data)

X = df[["Vibration"]]
y = df["Wear_Level"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)

predictions = model.predict(X_test)
error = mean_absolute_error(y_test, predictions)
print("Prediction Error:", error)
