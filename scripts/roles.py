import pandas as pd

# Define the roles data
roles_data = [
    #Executive Leadership Roles
    {"role_id": None, "role_name": "Chief Executive Officer", "description": "Leads the company", "salary_range_min": 200000.00, "salary_range_max": 500000.00},
    {"role_id": None, "role_name": "Chief Financial Officer", "description": "Manages company finances", "salary_range_min": 180000.00, "salary_range_max": 450000.00},
    {"role_id": None, "role_name": "Chief Human Resources Officer", "description": "Oversees HR strategies", "salary_range_min": 150000.00, "salary_range_max": 400000.00},
    {"role_id": None, "role_name": "Chief Marketing Officer", "description": "Directs marketing efforts", "salary_range_min": 160000.00, "salary_range_max": 420000.00},
    {"role_id": None, "role_name": "Chief Operating Officer", "description": "Oversees daily operations", "salary_range_min": 170000.00, "salary_range_max": 430000.00},
    {"role_id": None, "role_name": "Chief Security Officer", "description": "Manages security strategies", "salary_range_min": 160000.00, "salary_range_max": 420000.00},
    {"role_id": None, "role_name": "Chief Technology Officer", "description": "Oversees technology and innovation", "salary_range_min": 170000.00, "salary_range_max": 430000.00},
    #Director Roles
    {"role_id": None, "role_name": "Director of Business Development", "description": "Expands company business opportunities", "salary_range_min": 120000.00, "salary_range_max": 250000.00},
    {"role_id": None, "role_name": "Director of Customer Services", "description": "Leads customer service operations", "salary_range_min": 110000.00, "salary_range_max": 220000.00},
    {"role_id": None, "role_name": "Director of Finance", "description": "Oversees financial planning", "salary_range_min": 130000.00, "salary_range_max": 260000.00},
    {"role_id": None, "role_name": "Director of Human Resources", "description": "Manages HR policies and initiatives", "salary_range_min": 120000.00, "salary_range_max": 240000.00},
    {"role_id": None, "role_name": "Director of Information Technology", "description": "Manages IT infrastructure and strategies", "salary_range_min": 125000.00, "salary_range_max": 250000.00},
    {"role_id": None, "role_name": "Director of Operations", "description": "Oversees operational processes", "salary_range_min": 140000.00, "salary_range_max": 280000.00},
    {"role_id": None, "role_name": "Director of Sales", "description": "Leads sales strategy and team", "salary_range_min": 110000.00, "salary_range_max": 200000.00},
    #Managerial Roles
    {"role_id": None, "role_name": "Marketing Manager", "description": "Manages marketing campaigns and teams.", "salary_range_min": 75000.00, "salary_range_max": 120000.00},
    {"role_id": None, "role_name": "Media Manager", "description": "Oversees media planning and execution.", "salary_range_min": 70000.00, "salary_range_max": 115000.00},
    {"role_id": None, "role_name": "Information Systems Manager", "description": "Manages information systems and their development.", "salary_range_min": 90000.00, "salary_range_max": 130000.00},
    {"role_id": None, "role_name": "Human Resources Manager", "description": "Leads HR teams and initiatives.", "salary_range_min": 80000.00, "salary_range_max": 120000.00},
    {"role_id": None, "role_name": "Internal Auditor", "description": "Reviews and audits internal processes.", "salary_range_min": 60000.00, "salary_range_max": 90000.00},
    {"role_id": None, "role_name": "Assistant Manager", "description": "Assists in managing department operations.", "salary_range_min": 50000.00, "salary_range_max": 75000.00},
    #Specialist Roles
    {"role_id": None, "role_name": "Business Analyst", "description": "Analyzes business processes and strategies.", "salary_range_min": 65000.00, "salary_range_max": 85000.00},
    {"role_id": None, "role_name": "Senior Business Analyst", "description": "Leads analysis for complex business strategies.", "salary_range_min": 85000.00, "salary_range_max": 110000.00},
    {"role_id": None, "role_name": "Accountant", "description": "Manages financial records and compliance.", "salary_range_min": 55000.00, "salary_range_max": 75000.00},
    {"role_id": None, "role_name": "Senior Accountant", "description": "Oversees complex accounting tasks and team guidance.", "salary_range_min": 75000.00, "salary_range_max": 100000.00},
    {"role_id": None, "role_name": "Senior Cost Accountant", "description": "Specializes in cost accounting and analysis.", "salary_range_min": 80000.00, "salary_range_max": 105000.00},
    {"role_id": None, "role_name": "Cybersecurity Analyst", "description": "Protects systems against cybersecurity threats.", "salary_range_min": 85000.00, "salary_range_max": 120000.00},
    {"role_id": None, "role_name": "Information Security Officer", "description": "Manages security protocols and policies.", "salary_range_min": 95000.00, "salary_range_max": 130000.00},
    {"role_id": None, "role_name": "Database Administrator", "description": "Maintains and manages databases.", "salary_range_min": 75000.00, "salary_range_max": 95000.00},
    {"role_id": None, "role_name": "Senior Database Administrator", "description": "Oversees database infrastructure and strategy.", "salary_range_min": 95000.00, "salary_range_max": 125000.00},
    {"role_id": None, "role_name": "Data Coordinator", "description": "Manages and organizes data-related tasks.", "salary_range_min": 50000.00, "salary_range_max": 70000.00},
    #Technical Roles
    {"role_id": None, "role_name": "Software Developer I", "description": "Entry-level software development.", "salary_range_min": 60000.00, "salary_range_max": 80000.00},
    {"role_id": None, "role_name": "Software Developer II", "description": "Intermediate software development.", "salary_range_min": 80000.00, "salary_range_max": 100000.00},
    {"role_id": None, "role_name": "Software Developer III", "description": "Advanced software development.", "salary_range_min": 100000.00, "salary_range_max": 130000.00},
    {"role_id": None, "role_name": "Software Developer IV", "description": "Expert-level software development and leadership.", "salary_range_min": 130000.00, "salary_range_max": 160000.00},
    {"role_id": None, "role_name": "Engineer I", "description": "Entry-level engineering tasks.", "salary_range_min": 65000.00, "salary_range_max": 85000.00},
    {"role_id": None, "role_name": "Engineer II", "description": "Intermediate engineering responsibilities.", "salary_range_min": 85000.00, "salary_range_max": 105000.00},
    {"role_id": None, "role_name": "Engineer III", "description": "Advanced engineering projects.", "salary_range_min": 105000.00, "salary_range_max": 130000.00},
    {"role_id": None, "role_name": "Engineer IV", "description": "Expert-level engineering and leadership.", "salary_range_min": 130000.00, "salary_range_max": 160000.00},
    #Support Roles
    {"role_id": None, "role_name": "Administrative Assistant", "description": "Provides administrative support to teams.", "salary_range_min": 30000.00, "salary_range_max": 45000.00},
    {"role_id": None, "role_name": "Executive Administrative Assistant", "description": "Provides administrative support to executives.", "salary_range_min": 45000.00, "salary_range_max": 60000.00},
    {"role_id": None, "role_name": "Desktop Support Technician I", "description": "Entry-level desktop support.", "salary_range_min": 35000.00, "salary_range_max": 45000.00},
    {"role_id": None, "role_name": "Desktop Support Technician II", "description": "Intermediate desktop support.", "salary_range_min": 45000.00, "salary_range_max": 55000.00},
    {"role_id": None, "role_name": "Desktop Support Technician III", "description": "Advanced desktop support.", "salary_range_min": 55000.00, "salary_range_max": 70000.00},
    {"role_id": None, "role_name": "Desktop Support Technician IV", "description": "Expert desktop support and troubleshooting.", "salary_range_min": 70000.00, "salary_range_max": 90000.00},
    #Sales and Account Roles
    {"role_id": None, "role_name": "Account Coordinator", "description": "Coordinates client accounts.", "salary_range_min": 40000.00, "salary_range_max": 60000.00},
    {"role_id": None, "role_name": "Account Executive", "description": "Manages key client accounts.", "salary_range_min": 60000.00, "salary_range_max": 80000.00},
    {"role_id": None, "role_name": "Account Representative I", "description": "Entry-level client account management.", "salary_range_min": 35000.00, "salary_range_max": 45000.00},
    {"role_id": None, "role_name": "Account Representative II", "description": "Intermediate account management.", "salary_range_min": 45000.00, "salary_range_max": 55000.00},
    {"role_id": None, "role_name": "Account Representative III", "description": "Advanced account management.", "salary_range_min": 55000.00, "salary_range_max": 70000.00},
    {"role_id": None, "role_name": "Account Representative IV", "description": "Expert-level account management.", "salary_range_min": 70000.00, "salary_range_max": 90000.00},
    {"role_id": None, "role_name": "Sales Associate", "description": "Entry-level sales tasks.", "salary_range_min": 30000.00, "salary_range_max": 40000.00},
    {"role_id": None, "role_name": "Sales Representative", "description": "Manages client sales.", "salary_range_min": 40000.00, "salary_range_max": 60000.00},
]

# Convert to DataFrame
roles_df = pd.DataFrame(roles_data)

# Save to CSV
output_file = "data/roles.csv"
roles_df.to_csv(output_file, index=False)

print(f"Roles data saved to {output_file}")