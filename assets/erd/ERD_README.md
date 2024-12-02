<br>
<div style="text-align: center;">
<h1 style="font-weight: bold;">Employee Data Management System Documentation</h1>
</div>

## **Introduction**
The **Employee Data Management System** is a comprehensive database solution designed to manage employee information, organizational structure, projects, training, assets, payroll, and other core HR functionalities.

---

## **Project Goals**
The goals of the system are:
- To efficiently store and manage employee-related data, such as personal information, job roles, department assignments, and reporting structures.
- To track employee participation in training programs, projects, and benefits plans.
- To monitor company resource allocation (e.g., assets) and employee performance.
- To provide insights through a robust data model for business intelligence and reporting.
- To automate repetitive tasks and streamline workflows.

---

## **Entity-Relationship Diagram (ERD)**
The ERD visualizes the relational structure of the database. Below is a description of the key entities and their relationships.

---

## **Entity Descriptions and Attributes**

### **employees**
- **Primary Key**: `employee_id` (INT, AUTO_INCREMENT, NOT NULL)
- **Attributes**:
  - `first_name` (VARCHAR(50), NOT NULL)
  - `last_name` (VARCHAR(50), NOT NULL)
  - `date_of_birth` (DATE, NOT NULL)
  - `address` (VARCHAR(200), NULL)
  - `email` (VARCHAR(100), UNIQUE, NOT NULL)
  - `phone` (VARCHAR(15), NULL)
  - `hire_date` (DATE, NOT NULL)
  - `job_title` (VARCHAR(50), NOT NULL)
  - `status` (ENUM: `active`, `inactive`, NOT NULL)
- **Foreign Keys**:
  - `department_id` (INT, FK to `departments`, NOT NULL)
  - `role_id` (INT, FK to `roles`, NOT NULL)
  - `manager_id` (INT, Self-referencing FK to `employees`, NULL for top-level managers)

---

### **departments**
- **Primary Key**: `department_id` (INT, AUTO_INCREMENT, NOT NULL)
- **Attributes**:
  - `department_name` (VARCHAR(100), NOT NULL)
- **Foreign Keys**:
  - `location_id` (INT, FK to `regional_offices`, NOT NULL)
  - `manager_id` (INT, FK to `employees`, NULL)

---

### **regional_offices**
- **Primary Key**: `office_id` (INT, AUTO_INCREMENT, NOT NULL)
- **Attributes**:
  - `region_name` (VARCHAR(50), NOT NULL)
  - `country` (VARCHAR(50), NOT NULL)
  - `address` (VARCHAR(200), NOT NULL)
  - `currency` (VARCHAR(10), NOT NULL)

---

### **roles**
- **Primary Key**: `role_id` (INT, AUTO_INCREMENT, NOT NULL)
- **Attributes**:
  - `role_name` (VARCHAR(50), NOT NULL)
  - `description` (TEXT, NULL)
  - `salary_range_min` (DECIMAL(10, 2), NOT NULL)
  - `salary_range_max` (DECIMAL(10, 2), NOT NULL)

---

### **training_sessions**
- **Primary Key**: `training_id` (INT, AUTO_INCREMENT, NOT NULL)
- **Attributes**:
  - `topic` (VARCHAR(100), NOT NULL)
  - `description` (TEXT, NULL)
  - `date` (DATE, NOT NULL)
  - `duration` (INT, NOT NULL, in hours)
  - `instructor` (VARCHAR(100), NULL)
- **Foreign Key**:
  - `department_id` (INT, FK to `departments`, NOT NULL)

---

### **employee_training**
- **Primary Key**: `employee_training_id` (INT, AUTO_INCREMENT, NOT NULL)
- **Attributes**:
  - `completion_status` (ENUM: `completed`, `pending`, `failed`, NOT NULL)
  - `date_completed` (DATE, NULL)
- **Foreign Keys**:
  - `employee_id` (INT, FK to `employees`, NOT NULL)
  - `training_id` (INT, FK to `training_sessions`, NOT NULL)

---

### **benefits**
- **Primary Key**: `benefit_id` (INT, AUTO_INCREMENT, NOT NULL)
- **Attributes**:
  - `benefit_name` (VARCHAR(100), NOT NULL)
  - `description` (TEXT, NULL)
  - `cost_to_company` (DECIMAL(10, 2), NOT NULL)
  - `eligibility_criteria` (TEXT, NULL)

---

### **employee_benefits**
- **Primary Key**: `employee_benefit_id` (INT, AUTO_INCREMENT, NOT NULL)
- **Attributes**:
  - `enrollment_date` (DATE, NOT NULL)
  - `status` (ENUM: `active`, `inactive`, NOT NULL)
- **Foreign Keys**:
  - `employee_id` (INT, FK to `employees`, NOT NULL)
  - `benefit_id` (INT, FK to `benefits`, NOT NULL)

---

### **projects**
- **Primary Key**: `project_id` (INT, AUTO_INCREMENT, NOT NULL)
- **Attributes**:
  - `project_name` (VARCHAR(100), NOT NULL)
  - `start_date` (DATE, NOT NULL)
  - `end_date` (DATE, NULL)
  - `budget` (DECIMAL(15, 2), NULL)
- **Foreign Key**:
  - `department_id` (INT, FK to `departments`, NOT NULL)

---

### **employee_projects**
- **Primary Key**: `employee_project_id` (INT, AUTO_INCREMENT, NOT NULL)
- **Attributes**:
  - `project_role` (VARCHAR(100), NULL)
  - `hours_allocated` (DECIMAL(5, 2), NULL)
- **Foreign Keys**:
  - `employee_id` (INT, FK to `employees`, NOT NULL)
  - `project_id` (INT, FK to `projects`, NOT NULL)

---

### **payroll**
- **Primary Key**: `payroll_id` (INT, AUTO_INCREMENT, NOT NULL)
- **Attributes**:
  - `payment_date` (DATE, NOT NULL)
  - `gross_salary` (DECIMAL(10, 2), NOT NULL)
  - `tax_deductions` (DECIMAL(10, 2), NULL)
  - `net_salary` (DECIMAL(10, 2), NOT NULL)
  - `payment_status` (ENUM: `processed`, `failed`, NOT NULL)
- **Foreign Key**:
  - `employee_id` (INT, FK to `employees`, NOT NULL)

---

### **time_tracking**
- **Primary Key**: `time_entry_id` (INT, AUTO_INCREMENT, NOT NULL)
- **Attributes**:
  - `date` (DATE, NOT NULL)
  - `hours_worked` (DECIMAL(5, 2), NOT NULL)
  - `task_description` (TEXT, NULL)
- **Foreign Keys**:
  - `employee_id` (INT, FK to `employees`, NOT NULL)
  - `project_id` (INT, FK to `projects`, NOT NULL)

---

### **leave_management**
- **Primary Key**: `leave_id` (INT, AUTO_INCREMENT, NOT NULL)
- **Attributes**:
  - `leave_type` (ENUM: `sick`, `vacation`, `unpaid`, `other`, NOT NULL)
  - `start_date` (DATE, NOT NULL)
  - `end_date` (DATE, NOT NULL)
  - `approval_status` (ENUM: `approved`, `pending`, `rejected`, NOT NULL)
- **Foreign Key**:
  - `employee_id` (INT, FK to `employees`, NOT NULL)

---

### **performance_reviews**
- **Primary Key**: `review_id` (INT, AUTO_INCREMENT, NOT NULL)
- **Attributes**:
  - `review_date` (DATE, NOT NULL)
  - `overall_score` (DECIMAL(4, 2), NULL)
  - `comments` (TEXT, NULL)
- **Foreign Keys**:
  - `employee_id` (INT, FK to `employees`, NOT NULL)
  - `manager_id` (INT, FK to `employees`, NOT NULL)

---

### **assets**
- **Primary Key**: `asset_id` (INT, AUTO_INCREMENT, NOT NULL)
- **Attributes**:
  - `asset_name` (VARCHAR(100), NOT NULL)
  - `asset_type` (ENUM: `Desktop`, `Laptop`, `Tablet`, `Phone`, NOT NULL)
  - `purchase_date` (DATE, NOT NULL)
  - `status` (ENUM: `Assigned`, `Available`, `Maintenance`, `Retired`, NOT NULL)
- **Foreign Key**:
  - `assign_to` (INT, FK to employees, NULLABLE)

---

### **scheduled_tasks**
- **Primary Key**: `task_id` (INT, AUTO_INCREMENT, NOT NULL)
- **Attributes**:
  - `task_name` (VARCHAR(100), NOT NULL)
  - `frequency` (ENUM: `daily`, `weekly`, `monthly`, `yearly`, NOT NULL)
  - `last_run_date` (DATE, NULL)
  - `next_run_date` (DATE, NULL)
  - `status` (ENUM: `active`, `inactive`, NOT NULL)
- **Foreign Key**:
  - `employee_id` (INT, FK to employees, NOT NULL)

---

### **workflow_logs**
- **Primary Key**: `workflow_id` (INT, AUTO_INCREMENT, NOT NULL)
- **Attributes**:
  - `entity_name` (VARCHAR(50), NOT NULL)
  - `entity_id` (INT, NOT NULL)
  - `action_type` (ENUM: `create`, `update`, `delete`, NOT NULL)
  - `status` (ENUM: `active`, `inactive`, NOT NULL)
  - `timestamp` (DATETIME, NOT NULL)
- **Foreign Key**:
  - `performed_by` (INT, FK to `employees`, NOT NULL)

---

### **reports**
- **Primary Key**: `report_id` (INT, AUTO_INCREMENT, NOT NULL)
- **Attributes**:
  - `report_name` (VARCHAR(100), NOT NULL)
  - `created_date` (DATE, NOT NULL)
  - `last_run_date` (DATE, NULL)
- **Foreign Key**:
  - `created_by` (INT, FK to `employees`, NOT NULL)

---

### **access_control**
- **Primary Key**: `access_id` (INT, AUTO_INCREMENT, NOT NULL)
- **Attributes**:
  - `role` (ENUM: `admin`, `manager`, `employee`, NOT NULL)
  - `permissions` (JSON, NULL)
  - `last_login` (DATETIME, NULL)
- **Foreign Key**:
  - `employee_id` (INT, FK to `employees`, NOT NULL)

---

### **audit_logs**
- **Primary Key**: `log_id` (INT, AUTO_INCREMENT, NOT NULL)
- **Attributes**:
  - `entity_name` (VARCHAR(50), NOT NULL)
  - `action_type` (ENUM: `insert`, `update`, `delete`, NOT NULL)
  - `details` (TEXT, NULL)
  - `action_timestamp` (DATETIME, NOT NULL)
- **Foreign Key**:
  - `performed_by` (INT, FK to `employees`, NOT NULL)

---

## **Relationships Summary**
| **Source Table**         | **Destination Table**        | **Relationship Type**             | **Required?**      |
|--------------------------|------------------------------|-----------------------------------|--------------------|
| employees                | departments                  | One-to-Many                       | Yes                |
| employees                | roles                        | One-to-Many                       | Yes                |
| employees                | employees (Self-Referencing) | One-to-Many                       | No                 |
| departments              | regional_offices             | One-to-Many                       | Yes                |
| departments              | projects                     | One-to-Many                       | Yes                |
| departments              | training_sessions            | One-to-Many                       | Yes                |
| employees                | employee_training            | One-to-Many                       | Yes                |
| training_sessions        | employee_training            | One-to-Many                       | Yes                |
| employees                | training_sessions            | Many-to-Many (`employee_training`)| Yes                |
| projects                 | employee_projects            | One-to-Many                       | Yes                |
| employees                | employee_projects            | One-to-Many                       | Yes                |
| employees                | projects                     | Many-to-Many (`employee_projects`)| Yes                |
| employees                | employee_benefits            | One-to-Many                       | Yes                |
| benefits                 | employee_benefits            | One-to-Many                       | Yes                |
| employees                | benefits                     | Many-to-Many (`employee_benefits`)| Yes                |
| employees                | payroll                      | One-to-Many                       | Yes                |
| employees                | time_tracking                | One-to-Many                       | Yes                |
| projects                 | time_tracking                | One-to-Many                       | Yes                |
| employees                | leave_management             | One-to-Many                       | Yes                |
| employees                | performance_reviews          | One-to-Many                       | Yes                |
| employees                | assets                       | One-to-Many                       | No                 |
| employees                | workflow_logs                | One-to-Many                       | Yes                |
| employees                | scheduled_tasks              | One-to-Many                       | Yes                |
| employees                | audit_logs                   | One-to-Many                       | Yes                |
| workflow_logs            | employees                    | Many-to-One                       | Yes                |
| reports                  | employees                    | Many-to-One                       | Yes                |
| scheduled_tasks          | employees                    | Many-to-One                       | Yes                |

---

## **ERD Resources**

- **View the ERD Image**: [Employee Data Management ERD (.png)](erd-diagram.png)
- **Edit/View the Interactive ERD**: [_An editable version of this diagram can be shared upon request._]

---