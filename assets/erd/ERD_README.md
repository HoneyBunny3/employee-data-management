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
### **Employees**
- **Primary Key**: `employeeID`
- **Attributes**:
  - `firstName`, `lastName`, `email`, `phone`, `hireDate`, `jobTitle`
  - `departmentID (FK to Departments, REQUIRED)`
  - `roleID (FK to Roles, REQUIRED)`
  - `managerID (FK to Employees.employeeID, NULLABLE for top-level managers)`
  - `status (Active/Inactive)`
  - `address`
- **Purpose**: Core table for all employee-related data, including their assigned role.

### **Departments**
- **Primary Key**: `departmentID`
- **Attributes**: `departmentName`, `location (FK to Regional Offices, REQUIRED)`, `managerID (FK to Employees)`
- **Purpose**: Represents organizational units.

### **Regional Offices**
- **Primary Key**: `officeID`
- **Attributes**: `regionName`, `country`, `currency`, `address`
- **Purpose**: Represents geographical locations of the organization.

### **Roles**
- **Primary Key**: `roleID`
- **Attributes**: `roleName`, `salaryRangeMin`, `salaryRangeMax`, `description`
- **Purpose**: Tracks job titles and salary ranges.

### **Training Sessions**
- **Primary Key**: `trainingID`
- **Attributes**: `topic`, `description`, `date`, `duration`, `instructor`, `departmentID (FK to Departments, REQUIRED)`
- **Purpose**: Tracks company training programs.

### **Employee Training (Junction Table)**
- **Primary Key**: `employeeTrainingID`
- **Attributes**: `employeeID (FK to Employees, REQUIRED)`, `trainingID (FK to Training Sessions, REQUIRED)`, `completionStatus`, `dateCompleted`
- **Purpose**: Links employees to training sessions.

### **Projects**
- **Primary Key**: `projectID`
- **Attributes**: `projectName`, `startDate`, `endDate`, `budget`, `departmentID (FK to Departments, REQUIRED)`
- **Purpose**: Tracks company projects.

### **Employee Projects (Junction Table)**
- **Primary Key**: `employeeProjectID`
- **Attributes**: `employeeID (FK to Employees, REQUIRED)`, `projectID (FK to Projects, REQUIRED)`, `roleInProject`, `hoursAllocated`
- **Purpose**: Manages assignments of employees to projects.

### **Benefits**
- **Primary Key**: `benefitID`
- **Attributes**: `benefitName`, `description`, `costToCompany`, `eligibilityCriteria`
- **Purpose**: Represents company benefits.

### **Employee Benefits (Junction Table)**
- **Primary Key**: `employeeBenefitID`
- **Attributes**: `employeeID (FK to Employees, REQUIRED)`, `benefitID (FK to Benefits, REQUIRED)`, `enrollmentDate`, `status`
- **Purpose**: Tracks employee enrollment in benefits.

### **Payroll**
- **Primary Key**: `payrollID`
- **Attributes**: `employeeID (FK to Employees, REQUIRED)`, `paymentDate`, `grossSalary`, `taxDeductions`, `netSalary`, `paymentStatus`
- **Purpose**: Tracks employee payroll.

### **Time Tracking**
- **Primary Key**: `timeEntryID`
- **Attributes**: `employeeID (FK to Employees, REQUIRED)`, `projectID (FK to Projects, REQUIRED)`, `date`, `hoursWorked`, `taskDescription`
- **Purpose**: Tracks employee time allocation for tasks.

### **Leave Management**
- **Primary Key**: `leaveID`
- **Attributes**: `employeeID (FK to Employees, REQUIRED)`, `leaveType`, `startDate`, `endDate`, `approvalStatus`
- **Purpose**: Manages employee leave requests.

### **Performance Reviews**
- **Primary Key**: `reviewID`
- **Attributes**: `employeeID (FK to Employees, REQUIRED)`, `reviewDate`, `managerID (FK to Employees, REQUIRED)`, `overallScore`, `comments`
- **Purpose**: Stores employee performance evaluations.

### **Access Control**
- **Primary Key**: `accessID`
- **Attributes**: `employeeID (FK to Employees, REQUIRED)`, `role`, `lastLogin`, `permissions`
- **Purpose**: Manages system access control.

### **Assets**
- **Primary Key**: `assetID`
- **Attributes**: `assetName`, `assetType`, `purchaseDate`, `assignTo (FK to Employees, OPTIONAL)`, `status`
- **Purpose**: Tracks company-provided assets.

### **Audit Logs**
- **Primary Key**: `logID`
- **Attributes**: `entityName`, `actionType`, `actionTimestamp`, `performedBy (FK to Employees, REQUIRED)`, `details`
- **Purpose**: Tracks system actions for auditing purposes.

### **Reports**
- **Primary Key**: `reportID`
- **Attributes**: `reportName`, `createdBy (FK to Employees, REQUIRED)`, `createdDate`, `lastRunDate`
- **Purpose**: Tracks reports generated for business intelligence.

### **Workflow Logs**
- **Primary Key**: `workflowID`
- **Attributes**: `entityName`, `entityID`, `actionType`, `status`, `performedBy (FK to Employees, REQUIRED)`, `timestamp`
- **Purpose**: Tracks workflows and process improvements.

### **Scheduled Tasks**
- **Primary Key**: `taskID`
- **Attributes**: `taskName`, `frequency`, `lastRunDate`, `nextRunDate`, `status`
- **Purpose**: Automates routine system tasks.

---

## **Relationships Summary**
| **Source Table**         | **Destination Table**        | **Relationship Type**             | **Required?**      |
|---------------------------|------------------------------|------------------------------------|--------------------|
| Employees                 | Departments                 | One-to-Many                       | Yes                |
| Employees                 | Roles                       | One-to-Many                       | Yes                |
| Employees                 | Employees (Self-Referencing) | One-to-Many                       | No                 |
| Departments               | Regional Offices            | One-to-Many                       | Yes                |
| Departments               | Projects                    | One-to-Many                       | Yes                |
| Departments               | Training Sessions           | One-to-Many                       | Yes                |
| Employees                 | Access Control              | One-to-One                        | Yes                |
| Employees                 | Reports                     | One-to-Many                       | Yes                |
| Employees                 | Workflow Logs               | One-to-Many                       | Yes                |
| Employees                 | Scheduled Tasks             | One-to-Many                       | Yes                |
| Projects                  | Employee Projects           | One-to-Many                       | Yes                |
| Employees                 | Employee Projects           | One-to-Many                       | Yes                |
| Training Sessions         | Employee Training           | One-to-Many                       | Yes                |
| Benefits                  | Employee Benefits           | One-to-Many                       | Yes                |
| Projects                  | Time Tracking               | One-to-Many                       | Yes                |
| Employees                 | Time Tracking               | One-to-Many                       | Yes                |
| Employees                 | Leave Management            | One-to-Many                       | No                 |
| Employees                 | Payroll                     | One-to-Many                       | Yes                |
| Employees                 | Performance Reviews         | One-to-Many                       | No                 |
| Employees                 | Audit Logs                  | One-to-Many                       | Yes                |
| Employees                 | Assets                      | One-to-Many                       | No                 |

---

## ERD Resources

- **View the ERD Image**: [Employee Data Management ERD (.png)](erd-diagram.png)
- **Edit/View the Interactive ERD**: [_An editable version of this diagram can be shared upon request._]

---