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
- **Primary Key**: `employeeID` (AUTO_INCREMENT, NOT NULLABLE)
- **Attributes**:
  - `firstName` (VARCHAR(50), NOT NULLABLE)
  - `lastName` (VARCHAR(50), NOT NULLABLE)
  - `email` (VARCHAR(100), UNIQUE, NOT NULLABLE)
  - `phone` (VARCHAR(15), NULLABLE)
  - `hireDate` (DATE, NOT NULLABLE)
  - `jobTitle` (VARCHAR(50), NOT NULLABLE)
  - `status` (ENUM: `Active`, `Inactive`, NOT NULLABLE)
  - `address` (VARCHAR(255), NULLABLE)
- **Foreign Key**:
  - `departmentID` (FK to Departments, NOT NULLABLE)
  - `roleID` (FK to Roles, NOT NULLABLE)
  - `managerID` (Self-referencing FK to Employees, NULLABLE for top-level managers)

---

### **Departments**
- **Primary Key**: `departmentID` (AUTO_INCREMENT, NOT NULLABLE)
- **Attributes**:
  - `departmentName` (VARCHAR(100), NOT NULLABLE)
- **Foreign Key**:
  - `location` (FK to Regional Offices, NOT NULLABLE)
  - `managerID` (FK to Employees, NULLABLE)

---

### **Regional Offices**
- **Primary Key**: `officeID` (AUTO_INCREMENT, NOT NULLABLE)
- **Attributes**:
  - `regionName` (VARCHAR(50), NOT NULLABLE)
  - `country` (VARCHAR(50), NOT NULLABLE)
  - `currency` (VARCHAR(10), NOT NULLABLE)
  - `address` (VARCHAR(255), NOT NULLABLE)

---

### **Roles**
- **Primary Key**: `roleID` (AUTO_INCREMENT, NOT NULLABLE)
- **Attributes**:
  - `roleName` (VARCHAR(50), NOT NULLABLE)
  - `salaryRangeMin` (DECIMAL(10, 2), NOT NULLABLE)
  - `salaryRangeMax` (DECIMAL(10, 2), NOT NULLABLE)
  - `description` (TEXT, NULLABLE)

---

### **Training Sessions**
- **Primary Key**: `trainingID` (AUTO_INCREMENT, NOT NULLABLE)
- **Attributes**:
  - `topic` (VARCHAR(100), NOT NULLABLE)
  - `description` (TEXT, NULLABLE)
  - `date` (DATE, NOT NULLABLE)
  - `duration` (INT, NOT NULLABLE, in hours)
  - `instructor` (VARCHAR(100), NULLABLE)
- **Foreign Key**:
  - `departmentID` (FK to Departments, NOT NULLABLE)

---

### **Employee Training**
- **Primary Key**: `employeeTrainingID` (AUTO_INCREMENT, NOT NULLABLE)
- **Attributes**:
  - `completionStatus` (ENUM: `Completed`, `In Progress`, `Not Started`, NOT NULLABLE)
  - `dateCompleted` (DATE, NULLABLE)
- **Foreign Key**:
  - `employeeID` (FK to Employees, NOT NULLABLE)
  - `trainingID` (FK to Training Sessions, NOT NULLABLE)

---

### **Benefits**
- **Primary Key**: `benefitID` (AUTO_INCREMENT, NOT NULLABLE)
- **Attributes**:
  - `benefitName` (VARCHAR(100), NOT NULLABLE)
  - `description` (TEXT, NULLABLE)
  - `costToCompany` (DECIMAL(10, 2), NOT NULLABLE)
  - `eligibilityCriteria` (TEXT, NULLABLE)

---

### **Employee Benefits**
- **Primary Key**: `employeeBenefitID` (AUTO_INCREMENT, NOT NULLABLE)
- **Attributes**:
  - `enrollmentDate` (DATE, NOT NULLABLE)
  - `status` (ENUM: `Active`, `Inactive`, NOT NULLABLE)
- **Foreign Key**:
  - `employeeID` (FK to Employees, NOT NULLABLE)
  - `benefitID` (FK to Benefits, NOT NULLABLE)

---

### **Projects**
- **Primary Key**: `projectID` (AUTO_INCREMENT, NOT NULLABLE)
- **Attributes**:
  - `projectName` (VARCHAR(100), NOT NULLABLE)
  - `startDate` (DATE, NOT NULLABLE)
  - `endDate` (DATE, NULLABLE)
  - `budget` (DECIMAL(15, 2), NULLABLE)
- **Foreign Key**:
  - `departmentID` (FK to Departments, NOT NULLABLE)

---

### **Employee Projects**
- **Primary Key**: `employeeProjectID` (AUTO_INCREMENT, NOT NULLABLE)
- **Attributes**:
  - `roleInProject` (VARCHAR(100), NULLABLE)
  - `hoursAllocated` (DECIMAL(5, 2), NULLABLE)
- **Foreign Key**:
  - `employeeID` (FK to Employees, NOT NULLABLE)
  - `projectID` (FK to Projects, NOT NULLABLE)

---

### **Payroll**
- **Primary Key**: `payrollID` (AUTO_INCREMENT, NOT NULLABLE)
- **Attributes**:
  - `paymentDate` (DATE, NOT NULLABLE)
  - `grossSalary` (DECIMAL(10, 2), NOT NULLABLE)
  - `taxDeductions` (DECIMAL(10, 2), NULLABLE)
  - `netSalary` (DECIMAL(10, 2), NOT NULLABLE)
  - `paymentStatus` (ENUM: `Pending`, `Paid`, `Failed`, NOT NULLABLE)
- **Foreign Key**:
  - `employeeID` (FK to Employees, NOT NULLABLE)

---

### **Time Tracking**
- **Primary Key**: `timeEntryID` (AUTO_INCREMENT, NOT NULLABLE)
- **Attributes**:
  - `date` (DATE, NOT NULLABLE)
  - `hoursWorked` (DECIMAL(5, 2), NOT NULLABLE)
  - `taskDescription` (TEXT, NULLABLE)
- **Foreign Key**:
  - `employeeID` (FK to Employees, NOT NULLABLE)
  - `projectID` (FK to Projects, NOT NULLABLE)

---

### **Leave Management**
- **Primary Key**: `leaveID` (AUTO_INCREMENT, NOT NULLABLE)
- **Attributes**:
  - `leaveType` (ENUM: `Sick`, `Vacation`, `Unpaid`, `Other`, NOT NULLABLE)
  - `startDate` (DATE, NOT NULLABLE)
  - `endDate` (DATE, NOT NULLABLE)
  - `approvalStatus` (ENUM: `Pending`, `Approved`, `Rejected`, NOT NULLABLE)
- **Foreign Key**:
  - `employeeID` (FK to Employees, NOT NULLABLE)

---

### **Performance Reviews**
- **Primary Key**: `reviewID` (AUTO_INCREMENT, NOT NULLABLE)
- **Attributes**:
  - `reviewDate` (DATE, NOT NULLABLE)
  - `overallScore` (DECIMAL(3, 2), NULLABLE)
  - `comments` (TEXT, NULLABLE)
- **Foreign Key**:
  - `employeeID` (FK to Employees, NOT NULLABLE)
  - `managerID` (FK to Employees, NOT NULLABLE)

---

### **Assets**
- **Primary Key**: `assetID` (AUTO_INCREMENT, NOT NULLABLE)
- **Attributes**:
  - `assetName` (VARCHAR(100), NOT NULLABLE)
  - `assetType` (ENUM: `Desktop`, `Laptop`, `Tablet`, `Phone`, NOT NULLABLE)
  - `purchaseDate` (DATE, NOT NULLABLE)
  - `assignTo` (FK to Employees, NULLABLE)
  - `status` (ENUM: `Assigned`, `Available`, `Maintenance`, `Retired`, NOT NULLABLE)

---

### **Workflow Logs**
- **Primary Key**: `workflowID` (AUTO_INCREMENT, NOT NULLABLE)
- **Attributes**:
  - `entityName` (VARCHAR(50), NOT NULLABLE)
  - `entityID` (INT, NOT NULLABLE)
  - `actionType` (ENUM: `Create`, `Update`, `Delete`, NOT NULLABLE)
  - `status` (ENUM: `Active`, `Inactive`, NOT NULLABLE)
  - `timestamp` (DATETIME, NOT NULLABLE)
- **Foreign Key**:
  - `performedBy` (FK to Employees, NOT NULLABLE)

---

### **Scheduled Tasks**
- **Primary Key**: `taskID` (AUTO_INCREMENT, NOT NULLABLE)
- **Attributes**:
  - `taskName` (VARCHAR(100), NOT NULLABLE)
  - `frequency` (ENUM: `Daily`, `Weekly`, `Monthly`, `Yearly`, NOT NULLABLE)
  - `lastRunDate` (DATE, NULLABLE)
  - `nextRunDate` (DATE, NULLABLE)
  - `status` (ENUM: `Active`, `Inactive`, NOT NULLABLE)

---

### **Reports**
- **Primary Key**: `reportID` (AUTO_INCREMENT, NOT NULLABLE)
- **Attributes**:
  - `reportName` (VARCHAR(100), NOT NULLABLE)
  - `createdBy` (FK to Employees, NOT NULLABLE)
  - `createdDate` (DATE, NOT NULLABLE)
  - `lastRunDate` (DATE, NULLABLE)

---

### **Access Control**
- **Primary Key**: `accessID` (AUTO_INCREMENT, NOT NULLABLE)
- **Attributes**:
  - `employeeID` (FK to Employees, NOT NULLABLE)
  - `role` (ENUM: `Admin`, `Manager`, `Employee`, NOT NULLABLE)
  - `lastLogin` (DATETIME, NULLABLE)
  - `permissions` (JSON, NULLABLE)

---

### **Audit Logs**
- **Primary Key**: `logID` (AUTO_INCREMENT, NOT NULLABLE)
- **Attributes**:
  - `entityName` (VARCHAR(50), NOT NULLABLE)
  - `actionType` (ENUM: `Insert`, `Update`, `Delete`, NOT NULLABLE)
  - `actionTimestamp` (DATETIME, NOT NULLABLE)
  - `performedBy` (FK to Employees, NOT NULLABLE)
  - `details` (TEXT, NULLABLE)

---

## **Relationships Summary**
| **Source Table**         | **Destination Table**        | **Relationship Type**             | **Required?**      |
|---------------------------|------------------------------|------------------------------------|--------------------|
| Employees                 | Departments                 | One-to-Many                       | Yes                |
| Employees                 | Roles                       | One-to-Many                       | Yes                |
| Employees                 | Employees (Self-Referencing)| One-to-Many                       | No                 |
| Departments               | Regional Offices            | One-to-Many                       | Yes                |
| Departments               | Projects                    | One-to-Many                       | Yes                |
| Departments               | Training Sessions           | One-to-Many                       | Yes                |
| Employees                 | Employee Training           | One-to-Many                       | Yes                |
| Training Sessions         | Employee Training           | One-to-Many                       | Yes                |
| Projects                  | Employee Projects           | One-to-Many                       | Yes                |
| Employees                 | Employee Projects           | One-to-Many                       | Yes                |
| Employees                 | Employee Benefits           | One-to-Many                       | Yes                |
| Benefits                  | Employee Benefits           | One-to-Many                       | Yes                |
| Employees                 | Payroll                     | One-to-Many                       | Yes                |
| Employees                 | Time Tracking               | One-to-Many                       | Yes                |
| Projects                  | Time Tracking               | One-to-Many                       | Yes                |
| Employees                 | Leave Management            | One-to-Many                       | Yes                |
| Employees                 | Performance Reviews         | One-to-Many                       | Yes                |
| Employees                 | Assets                      | One-to-Many                       | No                 |
| Employees                 | Workflow Logs               | One-to-Many                       | Yes                |
| Employees                 | Scheduled Tasks             | One-to-Many                       | Yes                |
| Employees                 | Audit Logs                  | One-to-Many                       | Yes                |
| Workflow Logs             | Employees                   | Many-to-One                       | Yes                |
| Reports                   | Employees                   | Many-to-One                       | Yes                |
| Scheduled Tasks           | Employees                   | Many-to-One                       | Yes                |

---

## **ERD Resources**

- **View the ERD Image**: [Employee Data Management ERD (.png)](erd-diagram.png)
- **Edit/View the Interactive ERD**: [_An editable version of this diagram can be shared upon request._]

---