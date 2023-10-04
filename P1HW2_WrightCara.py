Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Travel Expense Calculator
... # October 3, 2023
... # CTI-110 P1HW2 - Travel Expense
... # Cara Wright
... 
... # Pseudocode:
... # 1. Ask the user to enter their budget.
... # 2. Ask the user to enter the travel destination.
... # 3. Ask the user for the amount they will spend on gas.
... # 4. Ask the user for the amount they will spend on accommodation.
... # 5. Ask the user for the amount they will spend on food.
... # 6. Add expenses to calculate the total expenses.
... # 7. Subtract total expenses from the budget to calculate the remaining budget.
... # 8. Display the results with explanations.
... 
... # Step 1: Ask user to enter their budget
... budget = float(input("Enter your budget: $"))
... 
... # Step 2: Ask user to enter travel destination
... destination = input("Enter your travel destination: ")
... 
... # Step 3: Ask user for the amount they will spend on gas
... gas_expense = float(input("Enter the amount you will spend on gas: $"))
... 
... # Step 4: Ask user for the amount they will spend on accommodation
... accommodation_expense = float(input("Enter the amount you will spend on accommodation: $"))
... 
... # Step 5: Ask user for the amount they will spend on food
... food_expense = float(input("Enter the amount you will spend on food: $"))
... 
... # Step 6: Add expenses to calculate the total expenses
... total_expenses = gas_expense + accommodation_expense + food_expense
... 
... # Step 7: Subtract expenses from the budget to calculate the remaining budget
... remaining_budget = budget - total_expenses
... 
# Step 8: Display results with explanations
print("\nTravel Information:")
print("Destination:", destination)
print("Budget: $", budget)
print("Gas Expense: $", gas_expense)
print("Accommodation Expense: $", accommodation_expense)
print("Food Expense: $", food_expense)

# Step 9: Display total expenses
print("\nTotal Expenses: $", total_expenses)

# Step 10: Display remaining budget
print("Remaining Budget: $", remaining_budget)


