Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # P3HW1_WrightCara.py
... # Cara Wright
... 
... # This program takes a number grade, determines the average, and displays the letter grade for the average.
... 
... # Initialize a list to store grades
... grades = []
... 
... # Enter grades for six modules and add them to the list
... mod_1 = float(input('Enter grade for Module 1: '))
... mod_2 = float(input('Enter grade for Module 2: '))
... mod_3 = float(input('Enter grade for Module 3: '))
... mod_4 = float(input('Enter grade for Module 4: '))
... mod_5 = float(input('Enter grade for Module 5: '))
... mod_6 = float(input('Enter grade for Module 6: '))
... 
... grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]
... 
... # Determine lowest, highest, sum, and average for grades
... low = min(grades)
... high = max(grades)
... total = sum(grades)
... avg = total / len(grades)
... 
... # Determine letter grade for the average
... if avg >= 90:
...     print('Your grade is: A')
... elif avg >= 80:
...     print('Your grade is: B')
... else:
...     print('Your grade is: F')
