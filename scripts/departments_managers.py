import pandas as pd

# Step 1: Define file paths
departments_file_path = "data/departments.csv"  # Path to the departments.csv file
employees_file_path = "data/employees.csv"  # Path to the employees.csv file
output_file_path = "data/departments_with_employees.csv"  # Output file path

# Step 2: Load the CSV files
departments_data = pd.read_csv(departments_file_path)
employees_data = pd.read_csv(employees_file_path)

# Step 3: Define department-to-manager mapping
department_to_manager_title = {
    "Accounting and Finance": "Chief Financial Officer",
    "Administration": "Chief Operating Officer",
    "Business Analysis": "Director of Business Development",
    "IT and Technology": "Chief Technology Officer",
    "Human Resources": "Chief Human Resources Officer",
    "Marketing and Media": "Chief Marketing Officer",
    "Sales": "Director of Sales",
    "Executive Leadership": "Chief Executive Officer",
}

# Step 4: Create a dictionary to map manager titles to employee IDs
manager_mapping = {}
for department, manager_title in department_to_manager_title.items():
    # Find the employee with the matching job_title
    matching_employee = employees_data[employees_data["job_title"] == manager_title]
    if not matching_employee.empty:
        manager_mapping[department] = matching_employee.iloc[0]["employee_id"]
    else:
        manager_mapping[department] = None  # If no match is found

# Step 5: Map manager IDs to the departments
departments_data["manager_id"] = departments_data["department_name"].map(manager_mapping)

# Step 6: Save the updated departments data with manager_id included
departments_data.to_csv(output_file_path, index=False)

print(f"Departments with managers have been saved to {output_file_path}")