import pandas as pd
import matplotlib.pyplot as plt

# Read dataset
Development = pd.read_csv("human-development-index.csv")

# Plot HDI values
Development["Human Development Index (UNDP)"].hist()

# Add title
plt.title("Distribution of Human Development Index")

# Label axes
plt.xlabel("HDI Value")
plt.ylabel("Frequency")

# Show graph
plt.show()
