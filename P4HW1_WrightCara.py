Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # CTI-110
... # P4HW1 - Score List
... # Cara Wright
... # 1DEC2023
... 
... # Pseudocode:
... # 1. Create an empty list named "scores" to store the scores.
... # 2. Ask the user to enter the number of scores they want to input.
... # 3. Create a loop to collect scores based on the user's input.
... #    a. Inside the loop, ask the user to enter a score.
... #    b. Validate if the entered score is between 0 and 100.
... #    c. If not, keep asking for a valid score using another loop.
... #    d. If valid, add the score to the "scores" list.
... # 4. Calculate the lowest score using the min() function on the "scores" list.
... # 5. Remove the lowest score from the list.
... # 6. Calculate the sum of scores by using the sum() function on the modified "scores" list.
... # 7. Calculate the average by dividing the sum of scores by the length of the modified "scores" list.
... # 8. Display the lowest score, modified score list, average, and the corresponding letter grade.
... 
... # Step 1: Create an empty list to store scores
... scores = []
... 
... # Step 2: Ask the user to enter the number of scores they want to input
... num_of_scores = int(input("Enter the number of scores you want to input: "))
... 
... # Step 3: Create a loop to collect scores
... for _ in range(num_of_scores):
...     # 3a. Ask the user to enter a score
...     score = float(input("Enter a score: "))
...     
...     # 3b. Validate if the entered score is between 0 and 100
...     while score < 0 or score > 100:
...         # 3c. If not, keep asking for a valid score
...         print("Invalid score. Please enter a score between 0 and 100.")
        score = float(input("Enter a valid score: "))
    
    # 3d. If valid, add the score to the "scores" list
    scores.append(score)

# Step 4: Calculate the lowest score
lowest_score = min(scores)

# Step 5: Remove the lowest score from the list
scores.remove(lowest_score)

# Step 6: Calculate the sum of scores
sum_of_scores = sum(scores)

# Step 7: Calculate the average
average = sum_of_scores / len(scores)

# Step 8: Display the results
print("\nLowest score entered:", lowest_score)
print("Score List after dropping lowest score:", scores)
print(f"Average: {average:.2f}")

# Determine the letter grade for the calculated average
if average >= 90:
    print("Letter Grade: A")
elif average >= 80:
    print("Letter Grade: B")
elif average >= 70:
    print("Letter Grade: C")
elif average >= 60:
    print("Letter Grade: D")
else:
    print("Letter Grade: F")
