<br>
<div style="text-align: center;">
<h1 style="font-weight: bold;">Database Table Creation Scripts</h1>
</div>

## **Introduction**

This document stores the _employee_management_ database table creation scripts. I created all 20 tables with their primary key, then I added the other rows and foreign key(s) to make craeting the tables easier.

## **Tables**

### **_employees_**

```sql
CREATE TABLE employees (
    employee_id INT AUTO_INCREMENT PRIMARY KEY
) ENGINE=InnoDB;
```

After all tables were created I used:

```sql
ALTER TABLE employees
ADD (
	first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    date_of_birth DATE NOT NULL,
    address VARCHAR(200),
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(15),
    hire_date DATE NOT NULL,
    job_title VARCHAR(50) NOT NULL,
    status ENUM('active', 'inactive') NOT NULL,
    department_id INT NOT NULL,
    role_id INT NOT NULL,
    manager_id INT,
    FOREIGN KEY (department_id) REFERENCES departments(department_id),
    FOREIGN KEY (role_id) REFERENCES roles(role_id),
    FOREIGN KEY (manager_id) REFERENCES employees(employee_id) ON DELETE SET NULL
);
```

---

### **_departments_**

```sql
CREATE TABLE departments (
    department_id INT AUTO_INCREMENT PRIMARY KEY
) ENGINE=InnoDB;
```
After all tables were created I used:

```sql
ALTER TABLE departments
ADD (
    department_name VARCHAR(100) NOT NULL,
    location_id INT NOT NULL,
    manager_id INT DEFAULT NULL,
    FOREIGN KEY (location_id) REFERENCES regional_offices(office_id),
    FOREIGN KEY (manager_id) REFERENCES employees(employee_id) ON DELETE SET NULL
);
```

---

### **_regional_offices_**

```sql
CREATE TABLE regional_offices (
    office_id INT AUTO_INCREMENT PRIMARY KEY
) ENGINE=InnoDB;
```

After all tables were created I used:

```sql
ALTER TABLE regional_offices
ADD (
    region_name VARCHAR(50) NOT NULL,
    country VARCHAR(50) NOT NULL,
    address VARCHAR(200) NOT NULL,
    currency VARCHAR(10) NOT NULL
);
```

---

### **_roles_**

```sql
CREATE TABLE roles (
    role_id INT AUTO_INCREMENT PRIMARY KEY
) ENGINE=InnoDB;
```

After all tables were created I used:

```sql
ALTER TABLE roles
ADD (
    role_name VARCHAR(50) NOT NULL,
    description TEXT DEFAULT NULL,
    salary_range_min DECIMAL(10, 2) NOT NULL,
    salary_range_max DECIMAL(10, 2) NOT NULL
);
```

---

### **_access_control_**


```sql
CREATE TABLE access_control (
    access_id INT AUTO_INCREMENT PRIMARY KEY
) ENGINE=InnoDB;
```

After all tables were created I used:

```sql
ALTER TABLE access_control
ADD (
    role ENUM('admin', 'manager', 'employee') NOT NULL,
    permissions JSON DEFAULT NULL,
    last_login DATETIME DEFAULT NULL,
    employee_id INT NOT NULL,
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id) ON DELETE CASCADE
);
```

---

### **_assets_**

```sql
CREATE TABLE assets (
    asset_id INT AUTO_INCREMENT PRIMARY KEY
) ENGINE=InnoDB;
```

After all tables were created I used:

```sql
ALTER TABLE assets
ADD (
    asset_name VARCHAR(100) NOT NULL,
    asset_type ENUM('desktop', 'laptop', 'tablet', 'phone') NOT NULL,
    purchase_date DATE NOT NULL,
    status ENUM('assigned', 'available', 'maintenance', 'retired') NOT NULL,
    assign_to INT DEFAULT NULL,
    FOREIGN KEY (assign_to) REFERENCES employees(employee_id) ON DELETE SET NULL
);
```

---

### **_audit_logs_**

```sql
CREATE TABLE audit_logs (
    log_id INT AUTO_INCREMENT PRIMARY KEY
) ENGINE=InnoDB;
```

After all tables were created I used:

```sql
ALTER TABLE audit_logs
ADD (
    entity_name VARCHAR(50) NOT NULL,
    action_type ENUM('insert', 'update', 'delete') NOT NULL,
    details TEXT DEFAULT NULL,
    action_timestamp DATETIME NOT NULL,
    performed_by INT NOT NULL,
    FOREIGN KEY (performed_by) REFERENCES employees(employee_id) ON DELETE CASCADE
);
```

---

### **_performance_reviews_**

```sql
CREATE TABLE performance_reviews (
    review_id INT AUTO_INCREMENT PRIMARY KEY
) ENGINE=InnoDB;
```

After all tables were created I used:

```sql
ALTER TABLE performance_reviews
ADD (
    review_date DATE NOT NULL,
    overall_score DECIMAL(4, 2) DEFAULT NULL,
    comments TEXT DEFAULT NULL,
    employee_id INT NOT NULL,
    manager_id INT DEFAULT NULL,
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id) ON DELETE CASCADE,
    FOREIGN KEY (manager_id) REFERENCES employees(employee_id) ON DELETE SET NULL
);
```

---

### **_leave_management_**

```sql
CREATE TABLE leave_management (
    leave_id INT AUTO_INCREMENT PRIMARY KEY
) ENGINE=InnoDB;
```

After all tables were created I used:

```sql
ALTER TABLE leave_management
ADD (
    leave_type ENUM('sick', 'vacation', 'unpaid', 'other') NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    approval_status ENUM('approved', 'pending', 'rejected') NOT NULL,
    employee_id INT NOT NULL,
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id) ON DELETE CASCADE
);
```

---

### **_time_tracking_**

```sql
CREATE TABLE time_tracking (
    time_entry_id INT AUTO_INCREMENT PRIMARY KEY
) ENGINE=InnoDB;
```

After all tables were created I used:

```sql
ALTER TABLE time_tracking
ADD (
    date DATE NOT NULL,
    hours_worked DECIMAL(5, 2) NOT NULL,
    task_description TEXT DEFAULT NULL,
    employee_id INT NOT NULL,
    project_id INT NOT NULL,
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id) ON DELETE CASCADE,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE
);
```

---

### **_payroll_**

```sql
CREATE TABLE payroll (
    payroll_id INT AUTO_INCREMENT PRIMARY KEY
) ENGINE=InnoDB;
```

After all tables were created I used:

```sql
ALTER TABLE payroll
ADD (
    payment_date DATE NOT NULL,
    gross_salary DECIMAL(10, 2) NOT NULL,
    tax_deductions DECIMAL(10, 2) DEFAULT NULL,
    net_salary DECIMAL(10, 2) NOT NULL,
    payment_status ENUM('processed', 'failed') NOT NULL,
    employee_id INT NOT NULL,
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id) ON DELETE CASCADE
);
```

---

### **_scheduled_tasks_**

```sql
CREATE TABLE scheduled_tasks (
    task_id INT AUTO_INCREMENT PRIMARY KEY
) ENGINE=InnoDB;
```
After all tables were created I used:

```sql
ALTER TABLE scheduled_tasks
ADD (
    task_name VARCHAR(100) NOT NULL,
    frequency ENUM('daily', 'weekly', 'monthly', 'yearly') NOT NULL,
    last_run_date DATE DEFAULT NULL,
    next_run_date DATE DEFAULT NULL,
    status ENUM('active', 'inactive') NOT NULL,
    employee_id INT NOT NULL,
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id) ON DELETE CASCADE
);
```

---

### **_workflow_logs_**

```sql
CREATE TABLE workflow_logs (
    workflow_id INT AUTO_INCREMENT PRIMARY KEY
) ENGINE=InnoDB;
```

After all tables were created I used:

```sql
ALTER TABLE workflow_logs
ADD (
    entity_name VARCHAR(50) NOT NULL,
    entity_id INT NOT NULL,
    action_type ENUM('create', 'update', 'delete') NOT NULL,
    status ENUM('active', 'inactive') NOT NULL,
    timestamp DATETIME NOT NULL,
    performed_by INT NOT NULL,
    FOREIGN KEY (performed_by) REFERENCES employees(employee_id) ON DELETE CASCADE
);
```

---

### **_reports_**

```sql
CREATE TABLE reports (
    report_id INT AUTO_INCREMENT PRIMARY KEY
) ENGINE=InnoDB;
```

After all tables were created I used:

```sql
ALTER TABLE reports
ADD (
    report_name VARCHAR(100) NOT NULL,
    created_date DATE NOT NULL,
    last_run_date DATE DEFAULT NULL,
    created_by INT NOT NULL,
    FOREIGN KEY (created_by) REFERENCES employees(employee_id) ON DELETE CASCADE
);
```

---

### **_training_sessions_**

```sql
CREATE TABLE training_sessions (
    training_id INT AUTO_INCREMENT PRIMARY KEY
) ENGINE=InnoDB;
```

After all tables were created I used:

```sql
ALTER TABLE training_sessions
ADD (
    topic VARCHAR(100) NOT NULL,
    description TEXT DEFAULT NULL,
    date DATE NOT NULL,
    duration INT NOT NULL, -- Duration in hours
    instructor VARCHAR(100) DEFAULT NULL,
    department_id INT NOT NULL,
    FOREIGN KEY (department_id) REFERENCES departments(department_id) ON DELETE CASCADE
);
```

---

### **_benefits_**

```sql
CREATE TABLE benefits (
    benefit_id INT AUTO_INCREMENT PRIMARY KEY
) ENGINE=InnoDB;
```

After all tables were created I used:

```sql
ALTER TABLE benefits
ADD (
    benefit_name VARCHAR(100) NOT NULL,
    description TEXT DEFAULT NULL,
    cost_to_company DECIMAL(10, 2) NOT NULL,
    eligibility_criteria TEXT DEFAULT NULL
);
```

---

### **_projects_**

```sql
CREATE TABLE projects (
    project_id INT AUTO_INCREMENT PRIMARY KEY
) ENGINE=InnoDB;
```

After all tables were created I used:

```sql
ALTER TABLE projects
ADD (
    project_name VARCHAR(100) NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE DEFAULT NULL,
    budget DECIMAL(15, 2) DEFAULT NULL,
    department_id INT NOT NULL,
    FOREIGN KEY (department_id) REFERENCES departments(department_id) ON DELETE CASCADE
);
```

---

### **_employee_training_ (Junction Table)**

```sql
CREATE TABLE employee_training (
    employee_training_id INT AUTO_INCREMENT PRIMARY KEY
) ENGINE=InnoDB;
```

After all tables were created I used:

```sql
ALTER TABLE employee_training
ADD (
    completion_status ENUM('completed', 'pending', 'failed') NOT NULL,
    date_completed DATE DEFAULT NULL,
    employee_id INT NOT NULL,
    training_id INT NOT NULL,
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id) ON DELETE CASCADE,
    FOREIGN KEY (training_id) REFERENCES training_sessions(training_id) ON DELETE CASCADE
);
```

---

### **_employee_benefits_ (Junction Table)**

```sql
CREATE TABLE employee_benefits (
    employee_benefit_id INT AUTO_INCREMENT PRIMARY KEY
) ENGINE=InnoDB;
```

After all tables were created I used:

```sql
ALTER TABLE employee_benefits
ADD (
    enrollment_date DATE NOT NULL,
    status ENUM('active', 'inactive') NOT NULL,
    employee_id INT NOT NULL,
    benefit_id INT NOT NULL,
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id) ON DELETE CASCADE,
    FOREIGN KEY (benefit_id) REFERENCES benefits(benefit_id) ON DELETE CASCADE
);
```

---

### **_employee_projects_ (Junction Table)**

```sql
CREATE TABLE employee_projects (
    employee_project_id INT AUTO_INCREMENT PRIMARY KEY
) ENGINE=InnoDB;
```

After all tables were created I used:

```sql
ALTER TABLE employee_projects
ADD (
    project_role VARCHAR(100) DEFAULT NULL,
    hours_allocated DECIMAL(5, 2) DEFAULT NULL,
    employee_id INT NOT NULL,
    project_id INT NOT NULL,
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id) ON DELETE CASCADE,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE
);
```

---