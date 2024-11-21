import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the file
file_path = "./dataSet.xlsx"
df = pd.read_excel(file_path, sheet_name=3)

# Generate and save the heatmap
plt.figure(figsize=(10, 8))  # Optional: Set figure size
sns.heatmap(df.isnull(), cbar=False, cmap="viridis")
plt.title("Dataset Completeness Heatmap")
plt.savefig("completeness_heatmap.png", dpi=300)  # Save the heatmap
plt.show()

# Plot percentage of missing data by column
missing_percentage = df.isnull().mean() * 100

plt.figure(figsize=(10, 5))  # Create a new figure for the bar chart
missing_percentage.plot(kind="bar")
plt.title("Percentage of Missing Data by Column")
plt.ylabel("Percentage")
plt.xlabel("Columns")
plt.savefig("missing_data_percentage.png", dpi=300)  # Save the bar chart
plt.show()

# Generate a completeness summary
completeness_summary = pd.DataFrame({
    "Total Rows": len(df),
    "Missing Values": df.isnull().sum(),
    "Missing Percentage": df.isnull().mean() * 100,
    "Complete Values": df.notnull().sum(),
})

print(completeness_summary)

