from sklearn.linear_model import LinearRegression
import numpy as np

# Sample maintenance data: [Machine Age (years), Failures]
X = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)  # Machine age
y = np.array([5, 7, 15, 18, 30])  # Failures

# Train model
model = LinearRegression()
model.fit(X, y)

# Predict failure rate for a 6-year-old machine
prediction = model.predict([[6]])
print("Predicted failures for a 6-year-old machine:", prediction[0])
