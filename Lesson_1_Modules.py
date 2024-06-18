# 1. Python Modules and Data Handling Assignment

# Objective: The aim of this assignment is to assess your understanding and ability to implement Python modules, both built-in and custom, and to apply data handling techniques using Python's data structures and error handling. This assignment will help solidify your grasp on creating and using modules, as well as manipulating and processing data effectively in Python.

# Task 1: Your Mood Today

# Problem Statement: Create a Python program using a custom module holding a function that asks the user how they are feeling today and responds with a custom message based on the mood entered. This function should then be imported and used in another file "main.py".

# Code Example:
    # mood_responses.py
    # def mood_response(mood):
        # Implement your response logic here

    # main.py
    # import mood_responses
    # mood = input("How are you feeling today? ")
    # print(mood_responses.mood_response(mood))

# Expected Outcome: The program should be able to take a user's mood as input (e.g., happy, sad, excited) and return a corresponding custom message.

from mood_responses import mood_response

def main():
    response = mood_response()
    print(response)

if __name__ == "__main__":
    main()