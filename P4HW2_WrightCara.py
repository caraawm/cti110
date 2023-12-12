# CTI-110
# P4HW2 - Salary Calculator
# Cara Wright
# 1DEC2023

# Pseudocode:
# 1. Initialize variables for total overtime pay, total regular pay, total gross pay, and number of employees.
# 2. Create a loop to enter employee information until the user enters "Done".
#    a. Inside the loop, ask the user for the employee's name.
#    b. If the user enters "Done", exit the loop.
#    c. Ask the user for the pay rate and hours worked.
#    d. Check for overtime and calculate overtime pay, regular pay, and gross pay.
#    e. Update the total overtime pay, total regular pay, total gross pay, and number of employees.
# 3. Display the total overtime pay, total regular pay, total gross pay, and number of employees.

# Step 1: Initialize variables
total_overtime_pay = 0
total_regular_pay = 0
total_gross_pay = 0
num_employees = 0

# Step 2: Create a loop to enter employee information
while True:
    # 2a: Ask for employee's name
    employee_name = input("Enter the employee's name (or 'Done' to finish): ")
    
    # 2b: If the user enters "Done", exit the loop
    if employee_name.lower() == "done":
        break
    
    # 2c: Ask for pay rate and hours worked
    pay_rate = float(input("Enter the employee's pay rate: "))
    hours_worked = float(input("Enter the number of hours the employee worked this week: "))
    
    # 2d: Check for overtime and calculate pay
    if hours_worked > 40:
        overtime_hours = hours_worked - 40
        overtime_pay = overtime_hours * (1.5 * pay_rate)
        regular_pay = 40 * pay_rate
        gross_pay = regular_pay + overtime_pay
    else:
        overtime_hours = 0
        overtime_pay = 0
        regular_pay = hours_worked * pay_rate
        gross_pay = regular_pay
    
    # 2e: Update totals
    total_overtime_pay += overtime_pay
    total_regular_pay += regular_pay
    total_gross_pay += gross_pay
    num_employees += 1

# Step 3: Display the results
print("\nSummary:")
print(f"Total Overtime Pay: ${total_overtime_pay:.2f}")
print(f"Total Regular Pay: ${total_regular_pay:.2f}")
print(f"Total Gross Pay: ${total_gross_pay:.2f}")
print(f"Number of Employees: {num_employees}")
