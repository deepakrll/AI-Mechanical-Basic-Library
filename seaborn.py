import seaborn as sns
import matplotlib.pyplot as plt

# Sample defect data
machine_ids = ['M1', 'M2', 'M3', 'M4']
defect_rates = [5.2, 6.1, 3.5, 4.0]

# Create barplot
sns.barplot(x=machine_ids, y=defect_rates, palette="Blues")
plt.xlabel("Machine ID")
plt.ylabel("Defect Rate (%)")
plt.title("Defect Rate Across Machines")
plt.show()
