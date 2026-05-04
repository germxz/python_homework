import csv

employees = []

with open("../csv/employees.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        employees.append(row)

names = [row['first_name'] + " " + row['last_name'] for row in employees]
print(names)

names_with_e = [name for name in names if "e" in name]

print(names_with_e)
