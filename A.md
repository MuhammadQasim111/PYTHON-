# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 11:28:22 2024

@author: Admin
"""

# We created a calculator assignment in the previous assignment. You need to update that calculator using functions. 
# Write a Python script for a calculator using functions.Create separate functions for addition, subtraction, multiplication, and division functions taking input as parameters and returning the result of the operation performed.Validate division by zero.Use input from the user to select an operation and numbers.Additionally, you can also create any more functions you like to improve the calculator functionality.





def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero is undefined"
    return x / y

def multiply(x, y):
    return x * y

def calculator():
    while True:
        print("\n1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        # Get user input for the operation
        option = input("Enter what you want: ")

        if option == '5':
            print("Exiting the calculator.")
            break   # if i dont perform break then  on entering 5, my program will not work

        # Check if the choice is valid
        if option in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input! Please enter numeric values.")
                continue

            # Perform the chosen operation
            if option == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif option == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            elif option == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            elif option == '4':
                print(f"{num1} / {num2} = {divide(num1, num2)}")
        else:
            print("Invalid choice! Please choose a valid operation.")

# Run the calculator
# if __name__ == "__main__":
#     calculator()
