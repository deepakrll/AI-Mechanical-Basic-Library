import matplotlib.pyplot as plt

# Sample stress and strain data
strain = [0, 0.01, 0.02, 0.03, 0.04, 0.05]
stress = [0, 50, 100, 120, 130, 125]  # In MPa

# Plot
plt.plot(strain, stress, marker='o', linestyle='-', color='b')
plt.xlabel('Strain')
plt.ylabel('Stress (MPa)')
plt.title('Stress-Strain Curve')
plt.grid(True)
plt.show()
