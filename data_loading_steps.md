# **Employee Data Management System Documentation**

## **Data Preparation and Processing Workflow**

### **Introduction**
This documentation outlines the steps taken to prepare, process, and manage the department and employee data for the **Employee Data Management System** project. It includes creating, merging, and enhancing datasets while ensuring consistency and alignment across various components.

---

Here’s a detailed documentation of the steps we took to create and manage the `regional_offices` table for your **Employee Data Management System** project:

---

# **Regional Offices Data Management**

## **Objective**
To define and populate the `regional_offices` table with data representing company locations across various regions. This table is foundational for assigning `location_id` values to departments.

---

## **Steps Taken**

### **1. Define the Structure of the `regional_offices` Table**

#### **Table Schema**
The table was designed with the following attributes:

| **Column Name**  | **Data Type**        | **Description**                                          |
|-------------------|----------------------|----------------------------------------------------------|
| `office_id`       | `INT` (Primary Key) | Unique identifier for each regional office.              |
| `region_name`     | `VARCHAR(50)`       | Name of the region where the office is located.          |
| `country`         | `VARCHAR(50)`       | Country where the office is located.                     |
| `address`         | `VARCHAR(200)`      | Full address of the office.                              |
| `currency`        | `VARCHAR(10)`       | Currency used in the region, e.g., USD, GBP, EUR.        |

---

### **2. Populate the `regional_offices` Data**

#### **Initial Data**
We started by populating the table with regional offices based on key company locations. The data included region names, countries, addresses, and currencies.

#### **Final List of Regional Offices**
The final dataset included the following regions:

| **office_id** | **region_name**      | **country**      | **address**                          | **currency** |
|---------------|----------------------|------------------|--------------------------------------|--------------|
| 1             | North America        | USA              | 123 Main St, New York, NY            | USD          |
| 2             | Europe               | UK               | 456 High St, London                  | GBP          |
| 3             | Asia                 | India            | 789 MG Road, Mumbai                  | INR          |
| 4             | South America        | Brazil           | 202 Paulista Ave, São Paulo          | BRL          |
| 5             | Australia            | Australia        | 101 George St, Sydney                | AUD          |
| 6             | East Asia            | Japan            | 606 Akihabara, Tokyo                 | JPY          |
| 7             | Africa               | South Africa     | 404 Nelson Mandela Blvd, Cape Town   | ZAR          |
| 8             | Scandinavia          | Sweden           | 707 Drottninggatan, Stockholm        | SEK          |
| 9             | Central America      | Mexico           | 505 Reforma, Mexico City             | MXN          |
| 10            | Eastern Europe       | Poland           | 808 Nowy Swiat, Warsaw               | PLN          |
| 11            | Southeast Asia       | Singapore        | 909 Orchard Rd, Singapore            | SGD          |
| 12            | Middle East          | UAE              | 1010 Sheikh Zayed Rd, Dubai          | AED          |
| 13            | Pacific Islands      | New Zealand      | 1313 Queen St, Auckland              | NZD          |
| 14            | Southern Europe      | Spain            | 1212 Gran Via, Madrid                | EUR          |
| 15            | Western Canada       | Canada           | 1111 Georgia St, Vancouver, BC       | CAD          |

---

### **3. Script to Populate the `regional_offices` Table**

Below is the Python script used to organize and save the data into a `.csv` file for the `regional_offices` table:

```python
import pandas as pd

# Define the regional offices data
regional_offices_data = [
    {"office_id": 1, "region_name": "North America", "country": "USA", "address": "123 Main St, New York, NY", "currency": "USD"},
    {"office_id": 2, "region_name": "Europe", "country": "UK", "address": "456 High St, London", "currency": "GBP"},
    {"office_id": 3, "region_name": "Asia", "country": "India", "address": "789 MG Road, Mumbai", "currency": "INR"},
    {"office_id": 4, "region_name": "South America", "country": "Brazil", "address": "202 Paulista Ave, São Paulo", "currency": "BRL"},
    {"office_id": 5, "region_name": "Australia", "country": "Australia", "address": "101 George St, Sydney", "currency": "AUD"},
    {"office_id": 6, "region_name": "East Asia", "country": "Japan", "address": "606 Akihabara, Tokyo", "currency": "JPY"},
    {"office_id": 7, "region_name": "Africa", "country": "South Africa", "address": "404 Nelson Mandela Blvd, Cape Town", "currency": "ZAR"},
    {"office_id": 8, "region_name": "Scandinavia", "country": "Sweden", "address": "707 Drottninggatan, Stockholm", "currency": "SEK"},
    {"office_id": 9, "region_name": "Central America", "country": "Mexico", "address": "505 Reforma, Mexico City", "currency": "MXN"},
    {"office_id": 10, "region_name": "Eastern Europe", "country": "Poland", "address": "808 Nowy Swiat, Warsaw", "currency": "PLN"},
    {"office_id": 11, "region_name": "Southeast Asia", "country": "Singapore", "address": "909 Orchard Rd, Singapore", "currency": "SGD"},
    {"office_id": 12, "region_name": "Middle East", "country": "UAE", "address": "1010 Sheikh Zayed Rd, Dubai", "currency": "AED"},
    {"office_id": 13, "region_name": "Pacific Islands", "country": "New Zealand", "address": "1313 Queen St, Auckland", "currency": "NZD"},
    {"office_id": 14, "region_name": "Southern Europe", "country": "Spain", "address": "1212 Gran Via, Madrid", "currency": "EUR"},
    {"office_id": 15, "region_name": "Western Canada", "country": "Canada", "address": "1111 Georgia St, Vancouver, BC", "currency": "CAD"},
]

# Convert to DataFrame
regional_offices_df = pd.DataFrame(regional_offices_data)

# Save to a CSV file
output_file_path = "data/regional_offices.csv"
regional_offices_df.to_csv(output_file_path, index=False)

print(f"Regional offices data has been saved to {output_file_path}")
```

---

### **4. Import Data into MySQL**

Once the data was saved to `regional_offices.csv`, we imported it into the MySQL `regional_offices` table using the following command:

```sql
LOAD DATA LOCAL INFILE 'data/regional_offices.csv'
INTO TABLE regional_offices
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"' 
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;
```

---

## **Next Steps**
1. Validate that all regional office data is correctly reflected in the database.
2. Link `regional_offices` to other tables, such as `departments`, for location-based assignments.


---

## **Steps Taken**

### **1. Assigning Managers to Departments**

#### **Goal**
To assign appropriate managers to each department using the `departments.csv` and `employees.csv` files.

#### **Steps**
1. **Mapped Departments to Manager Titles**:
   - Defined a mapping between `department_name` and the most relevant manager `job_title`.

   Example Mapping:
   - `Accounting and Finance` → `Chief Financial Officer`
   - `IT and Technology` → `Chief Technology Officer`

2. **Matched Manager Titles to Employee IDs**:
   - Used the `employees.csv` file to find the `employee_id` corresponding to the manager's `job_title`.

3. **Added Manager IDs to Departments**:
   - Updated the `departments.csv` file with the corresponding `manager_id` for each department.

#### **Output**
- **File**: `departments_with_employees.csv`
- **Columns**:
  - `department_id`
  - `department_name`
  - `location_id`
  - `manager_id`

---

### **2. Assigning Locations to Departments**

#### **Goal**
To associate each department with a specific `location_id` based on regional office assignments.

#### **Steps**
1. **Mapped Departments to Locations**:
   - Used `regional_offices.csv` to define `location_id` based on the region most appropriate for each department.

2. **Added Location IDs to Departments**:
   - Updated the `departments.csv` file with `location_id` values corresponding to each department.

#### **Output**
- **File**: `departments_with_locations.csv`
- **Columns**:
  - `department_id`
  - `department_name`
  - `location_id`

---

### **3. Merging Departments with Locations and Managers**

#### **Goal**
To consolidate `departments_with_employees.csv` and `departments_with_locations.csv` into a single file with both `manager_id` and `location_id` on the same row for each department.

#### **Steps**
1. **Merged Datasets**:
   - Combined the two datasets using a shared `department_id` column to ensure each department has a single row with both `manager_id` and `location_id`.

2. **Removed Duplicates**:
   - Ensured no redundant rows exist in the merged dataset.

3. **Ensured Consistency**:
   - Validated that all columns (`department_id`, `department_name`, `location_id`, `manager_id`) have correct and aligned data.

#### **Output**
- **File**: `merged_departments.csv`
- **Columns**:
  - `department_id`
  - `department_name`
  - `location_id`
  - `manager_id`

---

## **Python Scripts**

### **Assign Managers to Departments**
```python
import pandas as pd

# Paths to files
departments_file_path = "data/departments.csv"
employees_file_path = "data/employees.csv"
output_file_path = "data/departments_with_employees.csv"

# Load files
departments_data = pd.read_csv(departments_file_path)
employees_data = pd.read_csv(employees_file_path)

# Define department to manager mapping
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

# Match manager titles to employee IDs
manager_mapping = {}
for department, manager_title in department_to_manager_title.items():
    match = employees_data[employees_data["job_title"] == manager_title]
    manager_mapping[department] = match.iloc[0]["employee_id"] if not match.empty else None

# Update departments with manager IDs
departments_data["manager_id"] = departments_data["department_name"].map(manager_mapping)

# Save the result
departments_data.to_csv(output_file_path, index=False)
```

---

### **Merge Departments with Managers and Locations**
```python
import pandas as pd

# Paths to files
employees_file_path = "data/departments_with_employees.csv"
locations_file_path = "data/departments_with_locations.csv"
output_file_path = "data/merged_departments.csv"

# Load files
departments_with_employees = pd.read_csv(employees_file_path)
departments_with_locations = pd.read_csv(locations_file_path)

# Ensure consistency
departments_with_employees["manager_id"] = departments_with_employees["manager_id"].astype(int)
departments_with_locations["location_id"] = departments_with_locations["location_id"].astype(int)

# Merge datasets
merged_departments = pd.merge(
    departments_with_locations.drop(columns=["manager_id"]),
    departments_with_employees[["department_id", "manager_id"]],
    on="department_id",
    how="inner"
)

# Save the result
merged_departments.to_csv(output_file_path, index=False)
```

---

## **Next Steps**

1. **Validation**:
   - Review the final `merged_departments.csv` file to ensure correctness.

2. **Enhance Dataset**:
   - Incorporate additional fields like `department budget` or `performance metrics`.

3. **Automation**:
   - Package scripts into reusable modules or workflows.
