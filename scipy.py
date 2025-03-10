from scipy.optimize import minimize

# Objective function: Minimize material wastage
def objective(x):
    return x**2 + 4*x + 4  # Sample function

# Initial guess
x0 = [0]

# Perform optimization
result = minimize(objective, x0)
print("Optimal value:", result.x)
