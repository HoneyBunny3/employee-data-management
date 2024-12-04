import pandas as pd

# Step 1: Define file paths
departments_file = "data/departments.csv"  # Path to the departments.csv file
regional_offices_file = "data/regional_offices.csv"  # Path to the regional_offices.csv file
output_file = "data/departments_with_locations.csv"  # Output file path

# Step 2: Load the CSV files into DataFrames
departments_data = pd.read_csv(departments_file)
regional_offices_data = pd.read_csv(regional_offices_file)

# Step 3: Define department-to-location mapping (department_name -> office_id)
department_to_location_mapping = {
    "Accounting and Finance": 15,  # Australia, Australia
    "Administration": 2, # Asia, India
    "Business Analysis": 13, # Southeast Asia, Singapore
    "IT and Technology": 6, # Europe, UK
    "Human Resources": 14, # Western Canada, Canada
    "Marketing and Media": 4, #East Asia, Japan
    "Sales": 11, # South America, Brazil
    "Executive Leadership": 5 # Eastern Europe, Poland
}

# Step 4: Map location_id based on department_name
# Add a location_id column using the department-to-location mapping
departments_data["location_id"] = departments_data["department_name"].map(department_to_location_mapping)

# Step 5: Filter the final DataFrame to include only original columns from departments.csv
final_data = departments_data[["department_id", "department_name", "location_id", "manager_id"]]

# Step 6: Save the updated data to a new CSV file
final_data.to_csv(output_file, index=False)

print(f"Departments with locations have been saved to {output_file}")