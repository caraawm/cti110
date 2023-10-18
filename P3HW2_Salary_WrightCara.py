# CTI-110
# P3HW2 - Salary
# Cara Wright
# 18 October 2023

# Step 1: Ask the user to enter the name of the employee
employee_name = input("Enter the name of the employee: ")

# Step 2: Ask the user to enter the number of hours worked
hours_worked = float(input("Enter the number of hours the employee worked this week: "))

# Step 3: Ask the user to enter the pay rate
pay_rate = float(input("Enter the employee's pay rate: "))

# Step 4: Check for overtime
if hours_worked > 40:
    # Step 5a: Calculate overtime hours
    overtime_hours = hours_worked - 40
    # Step 5b: Calculate overtime pay
    overtime_pay = overtime_hours * (1.5 * pay_rate)
    # Step 5c: Calculate pay for regular hours
    regular_pay = 40 * pay_rate
    # Step 5d: Calculate gross pay
    gross_pay = regular_pay + overtime_pay
else:
    # Step 6: Calculate pay for regular hours
    regular_pay = hours_worked * pay_rate
    # Initialize overtime variables to zero
    overtime_hours = 0
    overtime_pay = 0
    # Step 7: Calculate gross pay
    gross_pay = regular_pay

# Step 8: Display the results
print(f"\nEmployee Name: {employee_name}")
print(f"Pay Rate: ${pay_rate:.2f} per hour")
print(f"Number of Hours Worked: {hours_worked:.2f} hours")
print(f"Overtime Hours: {overtime_hours:.2f} hours")
print(f"Overtime Pay: ${overtime_pay:.2f}")
print(f"Pay for Regular Hours: ${regular_pay:.2f}")
print(f"Gross Pay: ${gross_pay:.2f}")
