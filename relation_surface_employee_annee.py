import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load the data
file_path = "./dataSet.xlsx"  # Replace with the actual file path
df = pd.read_excel(file_path, sheet_name=3)

# Step 2: Ensure 'annee' is numeric
df['annee'] = pd.to_numeric(df['annee'], errors='coerce')

# Step 3: Aggregate data by year
# Assuming 'nb_exp' is the column for the number of workers and 'surfbio' for the exploited surface
evolution_data = df.groupby('annee')[['nb_exp', 'surfbio']].sum()

# Step 4: Calculate percentage evolution relative to the first year
evolution_percentage = evolution_data.apply(lambda x: (x / x.iloc[0] - 1) * 100)

# Step 5: Plot the data
plt.figure(figsize=(10, 6))
plt.plot(evolution_percentage.index, evolution_percentage['nb_exp'], marker="o", linestyle="-", color="blue", label="Number of Workers (%)")
plt.plot(evolution_percentage.index, evolution_percentage['surfbio'], marker="o", linestyle="--", color="green", label="Exploited Surface (%)")

# Add title and labels
plt.title("Percentage Evolution of Bio Agricole Workers and Exploited Surface Over Years in France")
plt.xlabel("Year")
plt.ylabel("Percentage Change (%)")
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.xticks(evolution_percentage.index, rotation=45)
plt.axhline(0, color="black", linewidth=0.8, linestyle="--")  # Add a horizontal line at 0% for reference
plt.legend()  # Add a legend to distinguish the lines
plt.tight_layout()

# Save and show the plot
plt.savefig("percentage_evolution_workers_vs_surface.png", dpi=300)
plt.show()
