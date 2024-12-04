import random
import csv

# Desired total entries
total_entries = 5000

# Original list of entries
entries = [
    "Account Coordinator", "Account Executive", "Account Representative I", "Account Representative II", 
    "Account Representative III", "Account Representative IV", "Administrative Assistant", 
    "Executive Administrative Assistant", "Business Analyst", "Senior Business Analyst", 
    "Data Coordinator", "Database Administrator", "Senior Database Administrator", 
    "Desktop Support Technician I", "Desktop Support Technician II", "Desktop Support Technician III", 
    "Desktop Support Technician IV", "Sales Associate", "Human Resources Assistant", 
    "Human Resources Manager", "Information Systems Manager", "Internal Auditor", 
    "Marketing Manager", "Media Manager", "Sales Representative", "Senior Cost Accountant", 
    "Accountant", "Senior Accountant", "Assistant Manager", "Cybersecurity Analyst", 
    "Information Security Officer", "Software Developer I", "Software Developer II", 
    "Software Developer III", "Software Developer IV", "Engineer I", "Engineer II", 
    "Engineer III", "Engineer IV"
]

# Calculate number of full repetitions and additional entries needed
full_repeats = total_entries // len(entries)
extra_entries = total_entries % len(entries)

# Duplicate the list
duplicated_entries = entries * full_repeats + random.sample(entries, extra_entries)

# Shuffle the list
random.shuffle(duplicated_entries)

# Define the output CSV file name
output_file = "randomized_entries.csv"

# Write the entries to a CSV file
with open(output_file, mode="w", newline="") as file:
    writer = csv.writer(file)
    # Optionally add a header
    writer.writerow(["Entry"])
    for entry in duplicated_entries:
        writer.writerow([entry])

print(f"CSV file '{output_file}' has been created with {len(duplicated_entries)} entries.")

assert len(duplicated_entries) == total_entries, "Error: The total entries do not match the expected count."