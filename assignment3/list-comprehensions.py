import csv

employees = []

with open("../csv/employees.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        employees.append(row)

# Skip header row and use indices for first and last name
names = [row[1] + " " + row[2] for row in employees[1:]]
print(names)

# Filter names that contain 'e'
names_with_e = [name for name in names if "e" in name]
print(names_with_e)
