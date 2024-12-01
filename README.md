<div style="text-align: center;">
<h1 style="font-weight: bold;">Employee Data Management</h1>
</div>

## **Introduction**
This project is designed to manage and store employee data for an organization. It allows for the tracking of employee information, including personal details, departments, roles, payroll, attendance, training, benefits, and project assignments. Additionally, the system handles asset management, workflow tracking, and audit logging for enhanced accountability.

The system is intended to showcase skills in database design, data management, and system development. It demonstrates the ability to create a robust relational database schema using MySQL, including defining entities, relationships, and managing employee-related data.

---

## **Features**
- Employee management (personal details, department, role, payroll, attendance)
- Department and regional office tracking
- Role and training management
- Payroll and leave tracking
- Asset and benefits management
- Project assignment and tracking
- Time tracking and leave management
- Scheduled task management
- Workflow logs for task progress and system process improvement
- Audit logs for system actions
- Comprehensive reporting for employee and organizational insights
- Regional office support and hierarchical structuring

---

## **Getting Started**

These instructions will help you set up the project locally for development and testing purposes.

### **Prerequisites**
- MySQL 8.0 or higher
- Git
- [MySQL Workbench](https://dev.mysql.com/downloads/workbench/) (optional but recommended for schema design)

### **Installation**
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/employee-data-management.git
   ```

2. **Navigate into the Project Folder**:
   ```bash
   cd employee-data-management
   ```

3. **Set Up Your MySQL Database**:
   - Create a new MySQL database (you can name it `employee_management`):
     ```sql
     CREATE DATABASE employee_management;
     ```
   - Import the initial database schema:
     ```bash
     mysql -u root -p employee_management < schema.sql
     ```

4. (Optional) Set up MySQL Workbench to visually manage the database schema.

---

## **Database Design**

The database is designed to store detailed information about employees, departments, roles, payroll, projects, training, benefits, assets, workflows, time tracking, and audit logging.

### **ERD (Entity Relationship Diagram)**
![ERD Diagram](assets/erd/erd-diagram.png)

---

### **Entities and Relationships**

#### **Core Entities**
- **employees**: Stores personal and professional employee data. Core entity linked to all other major functionalities.
- **departments**: Tracks organizational departments and their locations.
- **roles**: Stores job roles and salary ranges for employees.
- **regional_offices**: Tracks physical office locations globally.

#### **Payroll and Benefits**
- **payroll**: Tracks salary payments and deductions for employees.
- **benefits**: Lists employee benefit programs.
- **employee_benefits (Junction Table)**: Links employees to their enrolled benefits.

#### **Training and Performance**
- **training_sessions**: Tracks training programs conducted by the organization.
- **employee_training (Junction Table)**: Links employees to training sessions.
- **performance_reviews**: Tracks employee performance evaluations.

#### **Projects and Tasks**
- **projects**: Stores project details for organizational initiatives.
- **employee_projects (Junction Table)**: Links employees to projects.
- **scheduled_tasks**: Tracks recurring or one-time organizational tasks.
- **workflow_logs**: Tracks task progress and updates.

#### **Time and Leave Management**
- **time_tracking**: Logs work hours, breaks, and overtime for employees.
- **leave_management**: Tracks employee leave requests and approvals.

#### **Assets and System Management**
- **assets**: Tracks organizational assets assigned to employees.
- **access_control**: Manages system roles and permissions for employees.
- **audit_logs**: Records system actions for accountability.

#### **Reporting and Logs**
- **reports**: Tracks reports generated for organizational data insights.
- **audit_logs**: Tracks system changes and actions for security purposes.

---

### **Key Relationships**

- **employees ↔ departments**: One-to-Many
- **employees ↔ roles**: One-to-Many
- **employees ↔ payroll**: One-to-Many
- **employees ↔ benefits**: Many-to-Many
- **employees ↔ projects**: Many-to-Many
- **employees ↔ time_tracking**: One-to-Many
- **departments ↔ projects**: One-to-Many
- **scheduled Tasks ↔ workflow_logs**: One-to-Many
- **workflow Logs ↔ audit_logs**: One-to-Many

---

## **Development**

### **Employee Table Implementation**
The **employees** table includes the following columns:
- `employee_id`, `first_name`, `last_name`, `email`, `phone`, `hire_date`, `department_id`, `role_id`, `manager_id`, `status`, `address`.

### **Reporting**
The system enables the generation of comprehensive reports, using SQL JOIN queries across multiple tables, including but not limited to:
- Employee attendance
- Payroll summaries
- Department performance

---

### **Next Steps**
1. Complete data entry scripts for all 20 tables.
2. Test CRUD (Create, Read, Update, Delete) operations.
3. Design SQL queries for reports combining data across tables.
4. Validate relationships and indexing to optimize performance.

---

## **Contributing**

1. **Fork the Repository**:
   ```bash
   git clone https://github.com/your-username/employee-data-management.git
   ```

2. **Create Your Feature Branch**:
   ```bash
   git checkout -b feature-name
   ```

3. **Commit Your Changes**:
   ```bash
   git commit -am "Add new feature"
   ```

4. **Push to the Branch**:
   ```bash
   git push origin feature-name
   ```

5. **Create a New Pull Request** via GitHub.

---

## **License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---