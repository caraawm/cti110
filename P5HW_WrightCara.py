# P5HW - Math Quiz
# 7Dec2023
# CTI-110 P5HW - Math Quiz
# Cara Wright

import random

def generate_numbers():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    return num1, num2

def add_numbers():
    num1, num2 = generate_numbers()
    print(f"{num1} + {num2}")
    return num1 + num2

def subtract_numbers():
    num1, num2 = generate_numbers()
    print(f"{num1} - {num2}")
    return num1 - num2

def math_quiz():
    attempts = 0
    correct_answer = False

    while not correct_answer:
        print("MENU:")
        print("1. Add numbers")
        print("2. Subtract numbers")
        print("3. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            result = add_numbers()
        elif choice == "2":
            result = subtract_numbers()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
            continue

        user_answer = int(input("Enter your answer: "))
        attempts += 1

        if user_answer == result:
            print(f"Congratulations! You got it right in {attempts} attempts.")
            correct_answer = True
        else:
            if user_answer < result:
                print("Too low. Try again.")
            else:
                print("Too high. Try again.")

if __name__ == "__main__":
    math_quiz()
