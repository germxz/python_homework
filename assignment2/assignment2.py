import csv
import os



def read_employees():
    data = {}      
    rows = []      

    try:
        with open("../csv/employees.csv", "r") as file:
            reader = csv.reader(file)

            for i, row in enumerate(reader):
                if i == 0:
                    data["fields"] = row   
                else:
                    rows.append(row)       

        data["rows"] = rows
        return data
    except Exception as e:
        print(f"Error reading employees: {e}")
        return None
    
employees = read_employees()
print(employees)

def column_index(first_name):
    try:
        return employees["fields"].index(first_name)
    except Exception as e:
        print(f"Error finding column index for {first_name}: {e}")
        return None
employee_id_column = column_index("employee_id")
last_name_index = column_index("last_name")
employees["rows"] = sorted(employees["rows"], key=lambda row: row[last_name_index])

def first_name(row_number):
    try:
        index = column_index("first_name")
        return employees["rows"][row_number][index]
    except Exception as e:
        print(f"Error getting first name for row {row_number}: {e}")
        return None


def employee_find(employee_id):
    try:
        def employee_match(row):
            return int(row[employee_id_column]) == employee_id

        matches = list(filter(employee_match, employees["rows"]))
        return matches

    except Exception as e:
        print(f"Error finding employee {employee_id}: {e}")
        return []
    
def employee_find_2(employee_id):
    
    try:
        matches = [row for row in employees["rows"] if int(row[employee_id_column]) == employee_id]
        return matches
    except Exception as e:
        print(f"Error finding employee {employee_id} with list comprehension: {e}")
        return []

def sort_by_last_name():
    try:
        last_name_index = column_index("last_name")
        sorted_rows = sorted(employees["rows"], key=lambda row: row[last_name_index])
        return sorted_rows
    except Exception as e:
        print(f"Error sorting by last name: {e}")
        return []
    
def employee_dict(employee_row):
    try:
        fields = employees["fields"]
        return {field: employee_row[i] for i, field in enumerate(fields) if field != "employee_id"}
    except Exception as e:
        print(f"Error creating employee dict: {e}")
        return {}
    
def all_employees_dict():
    try:
        return {row[employee_id_column]: employee_dict(row) for row in employees["rows"]}
    except Exception as e:
        print(f"Error creating all employees dict: {e}")
        return {}

    
def get_this_value():
    return "ABC"



import custom_module

def set_that_secret(value):
    custom_module.set_that_secret(value)

import csv

def read_minutes():
    minutes1 = {}
    minutes2 = {}

    try:
        with open("../csv/minutes1.csv", "r") as f1:
            reader1 = csv.reader(f1)
            minutes1["fields"] = next(reader1)
            minutes1["rows"] = [tuple(row) for row in reader1]

        with open("../csv/minutes2.csv", "r") as f2:
            reader2 = csv.reader(f2)
            minutes2["fields"] = next(reader2)
            minutes2["rows"] = [tuple(row) for row in reader2]

        return minutes1, minutes2

    except Exception as e:
        print(e)
        return None, None