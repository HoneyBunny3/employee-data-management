import pandas as pd

# Step 1: Define file paths
employees_file_path = "data/departments_with_employees.csv"  # Path to departments_with_employees.csv
locations_file_path = "data/departments_with_locations.csv"  # Path to departments_with_locations.csv
output_file_path = "data/merged_departments.csv"  # Output file path

# Step 2: Load the CSV files into DataFrames
departments_with_employees = pd.read_csv(employees_file_path)
departments_with_locations = pd.read_csv(locations_file_path)

# Step 3: Ensure consistent data types
# Convert manager_id and location_id to integers for consistency
departments_with_employees["manager_id"] = departments_with_employees["manager_id"].fillna(0).astype(int)
departments_with_locations["location_id"] = departments_with_locations["location_id"].fillna(0).astype(int)

# Step 4: Merge the datasets, keeping only one manager_id column
merged_departments = pd.merge(
    departments_with_locations.drop(columns=["manager_id"]),  # Drop manager_id from locations data
    departments_with_employees[["department_id", "manager_id"]],  # Select only manager_id from employees data
    on="department_id",
    how="inner"
)

# Step 5: Remove any potential duplicates (just in case)
merged_departments = merged_departments.drop_duplicates()

# Step 6: Save the consolidated data to a new CSV file
merged_departments.to_csv(output_file_path, index=False)

print(f"Merged departments data has been saved to {output_file_path}")