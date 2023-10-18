# CTI-110
# P3HW1 - List
# Cara Wright
# 18 October 2023

# Pseudocode:
# 1. Create an empty list named "grades" to store the grades.
# 2. Ask the user to enter grades for six modules (Module 1 to Module 6) and append them to the "grades" list.
# 3. Calculate the lowest grade by using the min() function on the "grades" list.
# 4. Calculate the highest grade by using the max() function on the "grades" list.
# 5. Calculate the sum of grades by using the sum() function on the "grades" list.
# 6. Calculate the average by dividing the sum of grades by 6.
# 7. Display the lowest grade, highest grade, sum of grades, and average with the specified formatting.

# Step 1: Create an empty list to store grades
grades = []

# Step 2: Ask the user to enter grades for each module and append them to the list
grades.append(float(input("Enter grade for Module 1: "))

grades.append(float(input("Enter grade for Module 2: "))

grades.append(float(input("Enter grade for Module 3: "))

grades.append(float(input("Enter grade for Module 4: "))

grades.append(float(input("Enter grade for Module 5: "))

grades.append(float(input("Enter grade for Module 6: "))

# Step 3: Calculate the lowest grade
lowest_grade = min(grades)

# Step 4: Calculate the highest grade
highest_grade = max(grades)

# Step 5: Calculate the sum of grades
sum_of_grades = sum(grades)

# Step 6: Calculate the average
average = sum_of_grades / 6

# Step 7: Display the results with the specified formatting
print("\nModule 1:", grades[0])
print("Module 2:", grades[1])
print("Module 3:", grades[2])
print("Module 4:", grades[3])
print("Module 5:", grades[4])
print("Module 6:", grades[5])
print("\nLowest grade:", lowest_grade)
print("Highest grade:", highest_grade)
print("Sum of grades:", sum_of_grades)
print(f"Average: {average:.2f}")
