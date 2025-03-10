import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

# Generate synthetic manufacturing defect data
np.random.seed(0)
units_produced = np.linspace(100, 1000, 50)
defects = units_produced * 0.05 + np.random.normal(0, 5, 50)

# Build a simple regression model
model = tf.keras.Sequential([
    tf.keras.layers.Dense(1, input_shape=[1])
])

model.compile(optimizer='sgd', loss='mse')

# Train model
history = model.fit(units_produced, defects, epochs=100, verbose=0)

# Predict values
predicted_defects = model.predict(units_produced)

# Plot actual vs predicted
plt.scatter(units_produced, defects, label="Actual", color='red')
plt.plot(units_produced, predicted_defects, label="Predicted", color='blue')
plt.xlabel("Units Produced")
plt.ylabel("Defects")
plt.title("Defects Prediction using TensorFlow")
plt.legend()
plt.show()
