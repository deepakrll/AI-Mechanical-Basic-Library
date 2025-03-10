import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

# Generate synthetic manufacturing defect data
np.random.seed(0)
units_produced = np.linspace(100, 1000, 50)
defects = units_produced * 0.05 + np.random.normal(0, 5, 50)

# Reshape data to match TensorFlow expectations
units_produced = units_produced.reshape(-1, 1)
defects = defects.reshape(-1, 1)

# Define model using the corrected approach
model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(1,)),  # Corrected input shape definition
    tf.keras.layers.Dense(1)  # Single output neuron for regression
])

# Compile the model
model.compile(optimizer='sgd', loss='mse')

# Train the model
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
