from sympy import symbols, Eq, solve

# Define variables
F, A, σ = symbols('F A σ')

# Define equation (σ = F/A)
equation = Eq(σ, F / A)

# Solve for force when stress is 200 MPa and area is 0.005 m²
solution = solve(equation.subs({σ: 200, A: 0.005}), F)
print("Required Force:", solution[0], "N")
