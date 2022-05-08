# import module
import csv
import os
import subprocess

# Student List - We store the student list within this script as a dictionary to avoid re-editing the script when linking the path of the .csv file (which is more convenient).
# We will also use dict literal instead of dict constructor since it faster as it uses build_map and store_map instead of the generic call_function.
header = ['student_number', 'fname', 'lname', 'block']
data = [
    # Block X
    {'student_number': '123456789', 'fname': 'firstname', 'lname': 'lastname', 'block': 'X'},
    {'student_number': '123456789', 'fname': 'firstname', 'lname': 'lastname', 'block': 'X'}
]

# unique filename of csv
filename = "unique_filename.csv"

# Check and delete any existing file from variable filename before creating the list to avoid identity mismatch within the list.
if os.path.exists(filename):
    os.remove(filename)
else:
    None

# Write and create the student list from dictionary to csv file (after we create our temporary file, we can read it later and treat it as a ready-made csv).
with open(filename, 'w', encoding='UTF8', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=header)
    writer.writeheader()
    writer.writerows(data)

# Hide file to make it look clean
subprocess.check_call(["attrib", "+H", filename])

# Necessary variables
count = 0
student_block = None

# Input Options
print("Reminder: Sensitive input case! (Supports 'Sentence case', 'lowercase', and 'UPPERCASE')")
print("Search student according to: ")
print("[1] Student Number\n[2] First Name")
user_option = input("Enter desired option (1 or 2 only): ")

# Open newly created csv and read it then execute the commands according to the choice.
with open(filename, 'r') as student_list:
    reader = csv.reader(student_list, delimiter=',')
    if user_option == '1':
        student_number = input("Please enter the student number: ")
        # Force convert strings to uppercase to avoid errors in senstive lettercase.
        upper_student_number = student_number.upper()
        for row in reader:
            if upper_student_number == row[0]:
                first_name = row[1]
                last_name = row[2]
                student_block = row[3]
                print(first_name, last_name, "belongs to Block", student_block, ".")
                break
        if student_block is None:
            print("The student number entered is not included in the student list.")

    elif user_option == '2':
        first_name_2 = input("Please enter the first name: ")
        upper_first_name_2 = first_name_2.upper()
        for row in reader:
            if upper_first_name_2 == row[1]:
                count += 1
                last_name_2 = row[2]
                student_block = row[3]
        if count == 1:
            print(upper_first_name_2, last_name_2, "belongs to Block", student_block, ".")
        elif count > 1:
            print("There are", count, "students with the name", upper_first_name_2, ".")
            last_name_2 = input("Enter the last name of the student: ")
            upper_last_name_2 = last_name_2.upper()
            # Re-read the student list
            with open(filename, 'r') as student_list_2:
                reader = csv.reader(student_list_2, delimiter=',')
                for row in reader:
                    if upper_last_name_2 == row[2] and upper_first_name_2 == row[1]:
                        student_block = row[3]
                        print(upper_first_name_2, upper_last_name_2, "belongs to Block", student_block, ".")
        else:
            print("This name is not included in the student list.")

# Check and delete the temporarily made file of variable filename.
if os.path.exists(filename):
    os.remove(filename)
else:
    None

input("Press ENTER key to exit.")
