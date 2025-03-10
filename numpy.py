import numpy as np

# Define force (N) and area (m²)
force = np.array([500, 1000, 1500, 2000])  # Newtons
area = np.array([0.005, 0.005, 0.005, 0.005])  # Square meters

# Calculate stress (σ = F/A)
stress = force / area
print("Stress values in Pascals:", stress)
