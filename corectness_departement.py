import pandas as pd
import matplotlib.pyplot as plt
import requests



# Step 1: Fetch French departments from API
response = requests.get("https://geo.api.gouv.fr/departements")
if response.status_code == 200:
    french_departments = response.json()
else:
    raise Exception(f"Failed to fetch data from API: {response.status_code}")

# Extract department codes and names
department_codes = [dept["code"] for dept in french_departments]
department_names = [dept["nom"] for dept in french_departments]

# Combine codes and names into sets for validation
valid_department_codes = set(department_codes)
valid_department_names = set(department_names)

# Step 2: Load your DataFrame
file_path = "./dataSet.xlsx"
df = pd.read_excel(file_path, sheet_name=3)

# Step 3: Validate 'codedepartement' and 'departement'
df["Valid_Code"] = df["codedepartement"].isin(valid_department_codes)
df["Valid_Name"] = df["departement"].isin(valid_department_names)

# Step 4: Calculate Invalid Percentages
invalid_code_percentage = 100 * (~df["Valid_Code"]).mean()
invalid_name_percentage = 100 * (~df["Valid_Name"]).mean()

# Step 5: Prepare Data for Visualization
data = {
    "Invalid Percentage": [invalid_code_percentage, invalid_name_percentage]
}
columns = ["codedepartement", "departement"]

# Create DataFrame for Visualization
invalid_df = pd.DataFrame(data, index=columns)

# Step 6: Plot the Bar Chart
plt.figure(figsize=(8, 6))
invalid_df["Invalid Percentage"].plot(kind="bar", color="skyblue", edgecolor="black")
plt.title("Percentage of Invalid Department and Code Department")
plt.ylabel("Invalid Percentage (%)")
plt.xlabel("Columns")
plt.xticks(rotation=0)
plt.ylim(0, 100)  # Optional: Set Y-axis limits
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.tight_layout()

# Save the graph
plt.savefig("invalid_department_percentage.png", dpi=300)
plt.show()

# Step 1: Fetch French departments from API
response = requests.get("https://geo.api.gouv.fr/departements")
if response.status_code == 200:
    french_departments = response.json()
else:
    raise Exception(f"Failed to fetch data from API: {response.status_code}")

# Extract department codes and names
department_codes = {dept["code"] for dept in french_departments}
department_names = {dept["nom"] for dept in french_departments}

# Step 2: Load your DataFrame
file_path = "./dataSet.xlsx"
df = pd.read_excel(file_path, sheet_name=3)

# Step 3: Find Missing Departments
# Extract unique codes and names from your dataset
dataset_codes = set(df["codedepartement"].dropna())
dataset_names = set(df["departement"].dropna())

# Identify missing codes and names
missing_codes = department_codes - dataset_codes
missing_names = department_names - dataset_names

# Step 4: Summary of Missing Data
print(f"Missing department codes: {len(missing_codes)}")
print(f"Missing department names: {len(missing_names)}")

# Optional: Save missing departments to files
pd.DataFrame({"Missing Codes": list(missing_codes)}).to_csv("missing_codes.csv", index=False)
pd.DataFrame({"Missing Names": list(missing_names)}).to_csv("missing_names.csv", index=False)

# Step 5: Visualize the Results
categories = ["Present", "Missing"]
values_codes = [len(dataset_codes & department_codes), len(missing_codes)]
values_names = [len(dataset_names & department_names), len(missing_names)]

# Plot for codes
plt.figure(figsize=(8, 6))
plt.bar(categories, values_codes, color=["green", "red"], edgecolor="black")
plt.title("Coverage of Department Codes")
plt.ylabel("Count")
plt.savefig("department_code_coverage.png", dpi=300)
plt.show()

# Plot for names
plt.figure(figsize=(8, 6))
plt.bar(categories, values_names, color=["green", "red"], edgecolor="black")
plt.title("Coverage of Department Names")
plt.ylabel("Count")
plt.savefig("department_name_coverage.png", dpi=300)
plt.show()