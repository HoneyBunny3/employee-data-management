<div style="text-align: center;">
<h1 style="font-weight: bold;">Entity Relationships Explained</h1>
</div>

## **Entities and Relationships**

### **Employees and Departments**
Employees are the cornerstone of this system. Each employee is assigned to a single department, while a department can host multiple employees. This one-to-many relationship is crucial for managing organizational structure.

- **Type**: One-to-Many  
- **Key Columns**: `Employees.departmentID → Departments.departmentID`  
- **Real-World Example**:  
  - The HR department manages multiple employees, but each employee works under only one department.

---

### **Employees and Roles**
Each employee has a role within the organization, such as "Software Engineer" or "Manager." A single role can be assigned to multiple employees.

- **Type**: One-to-Many  
- **Key Columns**: `Employees.roleID → Roles.roleID`  
- **Real-World Example**:  
  - The "Manager" role applies to several employees overseeing their respective teams.

---

### **Employees Reporting to Managers**
The self-referencing relationship in the Employees table allows for a hierarchy where employees report to managers. Managers themselves are employees, enabling multi-level organizational charts.

- **Type**: One-to-Many (Self-Referencing)  
- **Key Columns**: `Employees.managerID → Employees.employeeID`  
- **Real-World Example**:  
  - Alice reports to Bob, who is a senior manager.

---

### **Departments and Regional Offices**
Departments are based in specific regional offices. Each regional office can host multiple departments.

- **Type**: One-to-Many  
- **Key Columns**: `Departments.location → RegionalOffices.officeID`  
- **Real-World Example**:  
  - The Engineering and Sales departments are located in the Austin regional office.

---

### **Employee Involvement in Projects**
Employees can participate in multiple projects, while each project can have multiple employees contributing. This many-to-many relationship is managed through the Employee Projects junction table.

- **Type**: Many-to-Many (via `Employee Projects` junction table)  
- **Key Columns**:  
  - `EmployeeProjects.employeeID → Employees.employeeID`  
  - `EmployeeProjects.projectID → Projects.projectID`  
- **Real-World Example**:  
  - Alice works on both the "Mobile App Development" and "Website Redesign" projects.

---

### **Project Tasks and Workflow Logs**
Each project consists of scheduled tasks that break the work into manageable chunks. Workflow logs track updates, changes, and activities for these tasks, ensuring all progress is monitored.

- **Type**: One-to-Many  
- **Key Columns**:  
  - `ScheduledTasks.projectID → Projects.projectID`  
  - `WorkflowLogs.entityID → ScheduledTasks.taskID`  
- **Real-World Example**:  
  - The "Website Redesign" project has tasks like "Create Wireframes" and "Develop Frontend," with each update logged in the workflow logs.

---

### **Employee Training**
Employees participate in various training sessions to enhance their skills. The Employee Training junction table connects employees to training sessions, creating a many-to-many relationship.

- **Type**: Many-to-Many (via `Employee Training` junction table)  
- **Key Columns**:  
  - `EmployeeTraining.employeeID → Employees.employeeID`  
  - `EmployeeTraining.trainingID → TrainingSessions.trainingID`  
- **Real-World Example**:  
  - Alice attended both "Leadership Development" and "Diversity Training."

---

### **Benefits Enrollment**
Employees can enroll in multiple benefit plans, such as health insurance or retirement plans. This many-to-many relationship is tracked using the Employee Benefits junction table.

- **Type**: Many-to-Many (via `Employee Benefits` junction table)  
- **Key Columns**:  
  - `EmployeeBenefits.employeeID → Employees.employeeID`  
  - `EmployeeBenefits.benefitID → Benefits.benefitID`  
- **Real-World Example**:  
  - Alice is enrolled in both the "Health Insurance Plan" and the "401(k) Retirement Plan."

---

### **Time Tracking**
Time tracking captures how employees allocate their hours across tasks and projects. Each employee logs time entries, which are linked to specific projects.

- **Type**: One-to-Many  
- **Key Columns**:  
  - `TimeTracking.employeeID → Employees.employeeID`  
  - `TimeTracking.projectID → Projects.projectID`  
- **Real-World Example**:  
  - Alice logs 8 hours for the "Website Redesign" project.

---

### **Asset Assignment**
The system tracks company assets assigned to employees, such as laptops or phones. Each asset can be assigned to one employee or marked as available, retired, or in maintenance.

- **Type**: One-to-Many  
- **Key Columns**: `Assets.assignTo → Employees.employeeID`  
- **Real-World Example**:  
  - Alice is assigned a company laptop and mobile phone.

---

### **Audit Logs and Access Control**
Audit logs track all actions performed in the system, providing a complete history of changes. Access control ensures employees have the right permissions, such as admin, manager, or employee-level access.

- **Audit Logs Key Columns**:  
  - `AuditLogs.performedBy → Employees.employeeID`  
  - `AuditLogs.entityID → ScheduledTasks.taskID`  
- **Access Control Key Columns**:  
  - `AccessControl.employeeID → Employees.employeeID`  
- **Real-World Example**:  
  - Bob, an admin, edits employee details, and the change is logged in the audit log.

---

### **Reporting**
Employees can generate reports summarizing system data, such as project progress, employee performance, or financial overviews.

- **Type**: One-to-Many  
- **Key Columns**: `Reports.createdBy → Employees.employeeID`  
- **Real-World Example**:  
  - Alice generates a quarterly performance review report.

---