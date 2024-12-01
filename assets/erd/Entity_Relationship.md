# Entity Relationships Explained

## **Employees → Departments**
- **Type**: One-to-Many
- **Key Columns**: `Employees.departmentID → Departments.departmentID`
- **Explanation**:
  - Each employee belongs to one department.
  - A department can have multiple employees.
- **Real-World Example**:
  - An HR department can have multiple employees, but each employee works in only one department.

---

## **Employees → Roles**
- **Type**: One-to-Many
- **Key Columns**: `Employees.roleID → Roles.roleID`
- **Explanation**:
  - Each employee has one assigned role.
  - A role can be assigned to multiple employees.
- **Real-World Example**:
  - Alice is assigned the "Software Engineer" role, while Bob is assigned the "Data Analyst" role.

---

## **Employees → Employees (Self-Referencing)**
- **Type**: One-to-Many
- **Key Columns**: `Employees.managerID → Employees.employeeID`
- **Explanation**:
  - Employees may report to a manager, who is also an employee.
  - A top-level manager will have a `NULL` value in `managerID`.
- **Real-World Example**:
  - An employee reports to their manager, and the manager reports to a senior manager, creating a hierarchy.

---

## **Departments → Regional Offices**
- **Type**: One-to-Many
- **Key Columns**: `Departments.location → RegionalOffices.officeID`
- **Explanation**:
  - Each department is based in one regional office.
  - A regional office can host multiple departments.
- **Real-World Example**:
  - The Engineering and Sales departments are located in the Austin regional office.

---

## **Employees ↔ Projects**
- **Type**: Many-to-Many (via `Employee Projects` junction table)
- **Key Columns**:
  - `EmployeeProjects.employeeID → Employees.employeeID`
  - `EmployeeProjects.projectID → Projects.projectID`
- **Explanation**:
  - Employees can work on multiple projects.
  - A project can involve multiple employees.
- **Real-World Example**:
  - A software engineer works on both the "Mobile App Development" and "Website Redesign" projects.

---

## **Employees ↔ Training Sessions**
- **Type**: Many-to-Many (via `Employee Training` junction table)
- **Key Columns**:
  - `EmployeeTraining.employeeID → Employees.employeeID`
  - `EmployeeTraining.trainingID → TrainingSessions.trainingID`
- **Explanation**:
  - Employees can participate in multiple training sessions.
  - A training session can include multiple employees.
- **Real-World Example**:
  - An employee attends both "Diversity Training" and "Leadership Development" sessions.

---

## **Employees ↔ Benefits**
- **Type**: Many-to-Many (via `Employee Benefits` junction table)
- **Key Columns**:
  - `EmployeeBenefits.employeeID → Employees.employeeID`
  - `EmployeeBenefits.benefitID → Benefits.benefitID`
- **Explanation**:
  - Employees can enroll in multiple benefit plans.
  - A benefit plan can be available to multiple employees.
- **Real-World Example**:
  - An employee enrolls in both the "Health Insurance Plan" and the "401(k) Retirement Plan."

---

## **Projects → Employee Projects**
- **Type**: One-to-Many
- **Key Columns**: `EmployeeProjects.projectID → Projects.projectID`
- **Explanation**:
  - A project can involve multiple records in the `Employee Projects` table.
  - Each record represents one employee's assignment to the project.
- **Real-World Example**:
  - The "Mobile App Development" project includes assignments for three employees: Alice, Bob, and Carol.

---

## **Employees → Employee Projects**
- **Type**: One-to-Many
- **Key Columns**: `EmployeeProjects.employeeID → Employees.employeeID`
- **Explanation**:
  - An employee can have multiple records in the `Employee Projects` table.
  - Each record represents an assignment to a specific project.
- **Real-World Example**:
  - Alice is assigned to two projects: "Mobile App Development" and "Website Redesign."

---

## **Training Sessions → Employee Training**
- **Type**: One-to-Many
- **Key Columns**: `EmployeeTraining.trainingID → TrainingSessions.trainingID`
- **Explanation**:
  - A training session can have multiple records in the `Employee Training` table.
  - Each record links the session to a specific employee.
- **Real-World Example**:
  - The "Leadership Development" training session is attended by 20 employees.

---

## **Benefits → Employee Benefits**
- **Type**: One-to-Many
- **Key Columns**: `EmployeeBenefits.benefitID → Benefits.benefitID`
- **Explanation**:
  - A benefit plan can have multiple records in the `Employee Benefits` table.
  - Each record links the plan to a specific employee.
- **Real-World Example**:
  - The "Health Insurance Plan" has 100 enrolled employees.

---

## **Projects → Workflow Logs**
- **Type**: One-to-Many
- **Key Columns**: `WorkflowLogs.projectID → Projects.projectID`
- **Explanation**:
  - Each workflow log entry belongs to one project.
  - A project can have multiple workflow log entries.
- **Real-World Example**:
  - The "Mobile App Development" project tracks workflow logs for sprint planning, testing, and deployment.

---

## **Employees → Workflow Logs**
- **Type**: One-to-Many
- **Key Columns**: `WorkflowLogs.employeeID → Employees.employeeID`
- **Explanation**:
  - Each workflow log entry is created or updated by an employee.
  - An employee can contribute to multiple workflow logs.
- **Real-World Example**:
  - Alice creates workflow log entries detailing her progress on the "Mobile App Development" project.

---

## **Workflow Logs → Audit Logs**
- **Type**: One-to-Many
- **Key Columns**: `AuditLogs.logID → WorkflowLogs.logID`
- **Explanation**:
  - Each workflow log action is tracked in the `Audit Logs` table.
  - Audit logs ensure accountability for updates made to workflow logs.
- **Real-World Example**:
  - An audit log tracks when Bob updated the timeline for a task in the workflow log.

---

## **Employees → Time Tracking**
- **Type**: One-to-Many
- **Key Columns**: `TimeTracking.employeeID → Employees.employeeID`
- **Explanation**:
  - An employee can have multiple time entries in the `Time Tracking` table.
  - Each entry records time spent on a specific project.
- **Real-World Example**:
  - Alice logs 8 hours on "Mobile App Development" and 4 hours on "Website Redesign."

---

## **Employees → Reports**
- **Type**: One-to-Many
- **Key Columns**: `Reports.createdBy → Employees.employeeID`
- **Explanation**:
  - An employee can generate multiple reports for tracking business insights.
- **Real-World Example**:
  - Alice generates quarterly performance and budget utilization reports.

---