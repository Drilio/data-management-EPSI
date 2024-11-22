import pandas as pd
import matplotlib.pyplot as plt

# Define the valid "code_groupe" values
valid_code_groupe = {"AU", "SF", "FR", "GCU", "LE", "PP", "VI", "HSAU"}

# Step 1: Load your DataFrame
file_path = "./dataSet.xlsx"  # Replace this with your actual file path
df = pd.read_excel(file_path, sheet_name=3)  # Adjust the sheet_name as needed

# Step 2: Validate "code_groupe"
df["Valid_Code_Groupe"] = df["code_groupe"].isin(valid_code_groupe)

# Step 3: Calculate Invalid Percentage
invalid_code_groupe_percentage = 100 * (~df["Valid_Code_Groupe"]).mean()

# Step 4: Prepare Data for Visualization
data = {
    "Invalid Percentage": [invalid_code_groupe_percentage]
}
columns = ["code_groupe"]

# Create DataFrame for Visualization
invalid_df = pd.DataFrame(data, index=columns)

# Step 5: Plot the Bar Chart
plt.figure(figsize=(8, 6))
invalid_df["Invalid Percentage"].plot(kind="bar", color="skyblue", edgecolor="black")
plt.title("Percentage of Invalid Code Groupe")
plt.ylabel("Invalid Percentage (%)")
plt.xlabel("Columns")
plt.xticks(rotation=0)
plt.ylim(0, 100)  # Optional: Set Y-axis limits
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.tight_layout()

# Save the graph
plt.savefig("invalid_code_groupe_percentage.png", dpi=300)
plt.show()

# Step 6: Identify Missing Codes
# Extract unique "code_groupe" from your dataset
dataset_code_groupe = set(df["code_groupe"].dropna())

# Identify missing "code_groupe"
missing_code_groupe = valid_code_groupe - dataset_code_groupe

# Summary of Missing Data
print(f"Missing code_groupe: {len(missing_code_groupe)}")
print(f"Missing code_groupe values: {missing_code_groupe}")

# Optional: Save missing "code_groupe" to a file
pd.DataFrame({"Missing Code Groupe": list(missing_code_groupe)}).to_csv("missing_code_groupe.csv", index=False)

# Step 7: Visualize Missing Data
categories = ["Present", "Missing"]
values = [len(dataset_code_groupe & valid_code_groupe), len(missing_code_groupe)]

plt.figure(figsize=(8, 6))
plt.bar(categories, values, color=["green", "red"], edgecolor="black")
plt.title("Coverage of Code Groupe")
plt.ylabel("Count")
plt.savefig("code_groupe_coverage.png", dpi=300)
plt.show()
