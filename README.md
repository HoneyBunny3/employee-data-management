# Employee Data Management

This project is designed to manage and store employee data for an organization. It allows for the tracking of employee information, including personal details, departments, roles, payroll, attendance, training, benefits, and project assignments. Additionally, the system handles asset management, workflow tracking, and audit logging for enhanced accountability.

The system is intended to showcase skills in database design, data management, and system development. It demonstrates the ability to create a robust relational database schema using MySQL, including defining entities, relationships, and managing employee-related data.

## Features:
- Employee management (personal details, department, role, payroll, attendance)
- Department and regional office tracking
- Role and training management
- Payroll and leave tracking
- Asset and benefits management
- Project assignment and tracking
- Workflow logs for task progress and system process improvement
- Audit logs for system actions

## Getting Started

These instructions will help you set up the project locally for development and testing purposes.

### Prerequisites:
- MySQL 8.0 or higher
- Git
- [MySQL Workbench](https://dev.mysql.com/downloads/workbench/) (optional but recommended for schema design)

### Installation:

Clone the repository:

```bash
git clone https://github.com/your-username/employee-data-management.git
```

Navigate into the project folder:

```bash
cd employee-data-management
```

Set up your MySQL database:

Create a new MySQL database (you can name it `employee_management`):

```sql
CREATE DATABASE employee_management;
```

Import the initial database schema (this can be added later when you finalize the design):

```bash
mysql -u root -p employee_management < schema.sql
```

(Optional) Set up MySQL Workbench to visually manage the database schema.

## Database Design

The database is designed to store detailed information about employees, departments, roles, payroll, projects, training, benefits, assets, and workflows.

### ERD (Entity Relationship Diagram)
![ERD Diagram](assets/erd/erd-diagram.png)

### Entities and Relationships:

- **Employees**: Core entity containing personal details, linked to roles, departments, payroll, attendance, training, projects, and benefits.
- **Departments**: Stores department information and is linked to employees, projects, and training sessions.
- **Roles**: Tracks job roles and salary ranges, linked to employees and access control.
- **Payroll**: Tracks salary payments and deductions for employees.
- **Projects**: Contains project details, linked to departments and employees.
- **Training Sessions**: Tracks training programs and employee participation.
- **Benefits**: Tracks benefit plans available to employees.
- **Assets**: Tracks organizational assets and their assignment to employees.
- **Workflow Logs**: Tracks employee task progress and workflow status for process improvement.
- **Audit Logs**: Records system actions performed by employees for auditing purposes.

### Key Relationships:

- **Employees ↔ Departments**: Many-to-One (An employee belongs to one department).
- **Employees ↔ Roles**: Many-to-One (An employee holds one role).
- **Employees ↔ Payroll**: One-to-Many (An employee can have many payroll records over time).
- **Employees ↔ Training Sessions**: Many-to-Many (An employee can participate in multiple training sessions).
- **Employees ↔ Projects**: Many-to-Many (An employee can work on multiple projects).
- **Departments ↔ Projects**: One-to-Many (A department can have many projects).
- **Employees ↔ Benefits**: Many-to-Many (An employee can enroll in multiple benefit plans).
- **Employees ↔ Assets**: One-to-Many (An employee can be assigned multiple assets).
- **Employees ↔ Workflow Logs**: One-to-Many (An employee creates multiple workflow logs).
- **Workflow Logs ↔ Audit Logs**: One-to-Many (Audit logs track workflow log updates).

## Development

### Employee Table Implementation:
The **Employees** table includes the following columns:
- `employeeID`, `firstName`, `lastName`, `email`, `phone`, `hireDate`, `departmentID`, `roleID`, `managerID`, `status`, `address`.

### Next Steps:
- Implement remaining tables like **Departments**, **Roles**, **Payroll**, **Projects**, **Training Sessions**, **Benefits**, and **Workflow Logs**.
- Write scripts to insert sample data into all tables.
- Test CRUD (Create, Read, Update, Delete) operations for managing employee data.
- Test JOIN queries for generating reports across entities.
- Validate workflow logs and audit log generation for task and system action tracking.

## Contributing

Fork the repository:

```bash
git clone https://github.com/your-username/employee-data-management.git
```

Create your feature branch:

```bash
git checkout -b feature-name
```

Commit your changes:

```bash
git commit -am "Add new feature"
```

Push to the branch:

```bash
git push origin feature-name
```

Create a new Pull Request via GitHub.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.