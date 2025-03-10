import pandas as pd

# Create sample manufacturing defect data
data = {'Machine ID': [101, 102, 103, 104],
        'Total Units': [1000, 1200, 950, 1100],
        'Defective Units': [50, 60, 30, 40]}

df = pd.DataFrame(data)

# Calculate defect rate
df['Defect Rate (%)'] = (df['Defective Units'] / df['Total Units']) * 100

print(df)
