Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# Travel Expense Calculator
# October 13, 2023
# CTI-110 P2HW1 - Travel
# Cara Wright

# Step 1: Ask the user to enter their budget
budget = float(input("Enter your budget: $"))

# Step 2: Ask the user to enter the travel destination
destination = input("Enter your travel destination: ")

# Step 3: Ask the user for the amount they will spend on gas
gas_expense = float(input("Enter the amount you will spend on gas: $"))

# Step 4: Ask the user for the amount they will spend on accommodation
accommodation_expense = float(input("Enter the amount you will spend on accommodation: $"))

# Step 5: Ask the user for the amount they will spend on food
food_expense = float(input("Enter the amount you will spend on food: $"))

# Step 6: Add expenses to calculate the total expenses
total_expenses = gas_expense + accommodation_expense + food_expense

# Step 7: Subtract total expenses from the budget to calculate the remaining budget
remaining_budget = budget - total_expenses

# Step 8: Display results with explanations
print("\nTravel Information:")
print(f"Destination: {destination}")
print(f"Budget: ${budget:.2f}")
print(f"Gas Expense: ${gas_expense:.2f}")
print(f"Accommodation Expense: ${accommodation_expense:.2f}")
print(f"Food Expense: ${food_expense:.2f")

# Step 9: Display total expenses
print(f"\nTotal Expenses: ${total_expenses:.2f}")

# Step 10: Display remaining budget
print(f"Remaining Budget: ${remaining_budget:.2f}")



